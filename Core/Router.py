#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sys, asyncio, inspect, logging, urllib.parse
import Const
from  App.Core.BaseController import BaseController
from aiohttp import web
import App.Middleware.Middleware as Middleware


def get_required_kw_args(fn):
    args = []
    params = inspect.signature(fn).parameters
    for name, param in params.items():
        if param.kind == inspect.Parameter.KEYWORD_ONLY and param.default == inspect.Parameter.empty:
            args.append(name)
    return tuple(args)


def get_named_kw_args(fn):
    args = []
    params = inspect.signature(fn).parameters
    for name, param in params.items():
        if param.kind == inspect.Parameter.KEYWORD_ONLY:
            args.append(name)
    return tuple(args)


def has_named_kw_args(fn):
    params = inspect.signature(fn).parameters
    for name, param in params.items():
        if param.kind == inspect.Parameter.KEYWORD_ONLY:
            return True


def has_var_kw_arg(fn):
    params = inspect.signature(fn).parameters
    for name, param in params.items():
        if param.kind == inspect.Parameter.VAR_KEYWORD:
            return True


def has_request_arg(fn):
    sig = inspect.signature(fn)
    params = sig.parameters
    found = False
    for name, param in params.items():
        if name == 'request':
            found = True
            continue
        if found and (param.kind != inspect.Parameter.VAR_POSITIONAL and param.kind != inspect.Parameter.KEYWORD_ONLY and param.kind != inspect.Parameter.VAR_KEYWORD):
            raise ValueError('request parameter must be the last named parameter in function: %s%s' % (fn.__name__, str(sig)))
    return found

class RequestHandler(object):

    def __init__(self, app, module, fn):
        self._app = app
        self._func = fn
        self._module = module
        self._has_request_arg = has_request_arg(fn)
        self._has_var_kw_arg = has_var_kw_arg(fn)
        self._has_named_kw_args = has_named_kw_args(fn)
        self._named_kw_args = get_named_kw_args(fn)
        self._required_kw_args = get_required_kw_args(fn)

    def __call__(self, request):
        # if hasattr(self._module(), 'middlewares'):
        #     middle = getattr(self._module(), 'middlewares')
        #     middlePass = None
        #     for func in middle:
        #         fn = getattr(Middleware, func)
        #         middlePass = fn(request)
        #         if (middlePass != None):
        #             break
        #     if (middlePass != None):
        #         return middlePass
        #
        # kw = None
        # if self._has_var_kw_arg or self._has_named_kw_args or self._required_kw_args:
        #     if request.method == 'POST':
        #         if not request.content_type:
        #             return web.HTTPBadRequest('Missing Content-Type.')
        #         ct = request.content_type.lower()
        #         if ct.startswith('application/json'):
        #             params = yield from request.json()
        #             if not isinstance(params, dict):
        #                 return web.HTTPBadRequest('JSON body must be object.')
        #             kw = params
        #         elif ct.startswith('application/x-www-form-urlencoded') or ct.startswith('multipart/form-data'):
        #             params = yield from request.post()
        #             kw = dict(**params)
        #         else:
        #             return web.HTTPBadRequest('Unsupported Content-Type: %s' % request.content_type)
        #     if request.method == 'GET':
        #         qs = request.query_string
        #         if qs:
        #             kw = dict()
        #             for k, v in urllib.parse.parse_qs(qs, True).items():
        #                 kw[k] = v[0]
        # if kw is None:
        #     kw = dict(**request.match_info)
        # else:
        #     if not self._has_var_kw_arg and self._named_kw_args:
        #         # remove all unamed kw:
        #         copy = dict()
        #         for name in self._named_kw_args:
        #             if name in kw:
        #                 copy[name] = kw[name]
        #         kw = copy
        #     # check named arg:
        #     for k, v in request.match_info.items():
        #         if k in kw:
        #             logging.warning('Duplicate arg name in named arg and kw args: %s' % k)
        #         kw[k] = v
        # if self._has_request_arg:
        #     kw['request'] = request
        # # check required kw:
        # if self._required_kw_args:
        #     for name in self._required_kw_args:
        #         if not name in kw:
        #             return web.HTTPBadRequest('Missing argument: %s' % name)
        # logging.info('call with args: %s' % str(kw))
        # try:
        #     # r = await self._module.self._func(**kw)
        #     # func = getattr(self._module,self._func)
        #     r = yield from self._func(**kw)
        #     return r
        # except Exception as e:
        #     print(e)
        #     return web.Response(body='<h1>请求异常</h1>', content_type='text/html')
        return self.callFunc(request)

    async def callFunc(self, request):
        if hasattr(self._module(), 'middlewares'):
            middle = getattr(self._module(), 'middlewares')
            middlePass = None
            for func in middle:
                fn = getattr(Middleware, func)
                middlePass = fn(request)
                if (middlePass != None):
                    break
            if (middlePass != None):
                return middlePass

        kw = None
        if self._has_var_kw_arg or self._has_named_kw_args or self._required_kw_args:
            if request.method == 'POST':
                if not request.content_type:
                    return web.HTTPBadRequest('Missing Content-Type.')
                ct = request.content_type.lower()
                if ct.startswith('application/json'):
                    params = await request.json()
                    if not isinstance(params, dict):
                        return web.HTTPBadRequest('JSON body must be object.')
                    kw = params
                elif ct.startswith('application/x-www-form-urlencoded') or ct.startswith('multipart/form-data'):
                    params = await request.post()
                    kw = dict(**params)
                else:
                    return web.HTTPBadRequest('Unsupported Content-Type: %s' % request.content_type)
            if request.method == 'GET':
                qs = request.query_string
                if qs:
                    kw = dict()
                    for k, v in urllib.parse.parse_qs(qs, True).items():
                        kw[k] = v[0]
        if kw is None:
            kw = dict(**request.match_info)
        else:
            if not self._has_var_kw_arg and self._named_kw_args:
                # remove all unamed kw:
                copy = dict()
                for name in self._named_kw_args:
                    if name in kw:
                        copy[name] = kw[name]
                kw = copy
            # check named arg:
            for k, v in request.match_info.items():
                if k in kw:
                    logging.warning('Duplicate arg name in named arg and kw args: %s' % k)
                kw[k] = v
        if self._has_request_arg:
            kw['request'] = request
        # check required kw:
        if self._required_kw_args:
            for name in self._required_kw_args:
                if not name in kw:
                    return web.HTTPBadRequest('Missing argument: %s' % name)
        logging.info('call with args: %s' % str(kw))
        try:
            # r = await self._module.self._func(**kw)
            # func = getattr(self._module,self._func)
            print(self._func)
            r = await self._func(**kw)
            return r
        except Exception as e:
            print(e)
            return web.Response(body='<h1>请求异常</h1>', content_type='text/html')

def get_file_path(dir, mod):
    for x in os.listdir(dir):
        newdir = dir + '/' + x
        if(os.path.isdir(newdir)):
            get_file_path(newdir, mod)

        if(os.path.isfile(newdir) and os.path.splitext(newdir)[1] == '.py'
         and os.path.split(newdir)[1] != '__init__.py'):
            mod.append(newdir)

def add_route(app, module, fn):
    method = getattr(fn, '__method__', None)
    path = getattr(fn, '__route__', None)
    if not asyncio.iscoroutinefunction(fn) and not inspect.isgeneratorfunction(fn):
        fn = asyncio.coroutine(fn)
    app.router.add_route(method, path, RequestHandler(app, module, fn))

def add_static(app):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
    app.router.add_static('/static/', path)


def add_routes(app):
    mod = []
    get_file_path(Const.AppPath + 'Controllers', mod)
    appPathLen = len(Const.AppPath)
    for attr in mod:
        atr = 'App.' + os.path.splitext(attr[appPathLen:])[0].replace('/', '.')
        control = atr[atr.rfind('.') + 1:]
        module = getattr(__import__(atr, globals(), locals(), control), control)
        # obj = module.__class__()
        # print(obj)
        theMembers = BaseController.getFuncs(module)
        for func in theMembers:
            fn = getattr(module(), func)
            if callable(fn):
                method = getattr(fn, '__method__', None)
                path = getattr(fn, '__route__', None)
                if method and path:
                    add_route(app, module, fn)


    #    print(theMembers)
        # if attr.startswith('_'):
        #     continue
        # fn = getattr(mod, attr)
        # if callable(fn):
        #     method = getattr(fn, '__method__', None)
        #     path = getattr(fn, '__route__', None)
        #     if method and path:
        #         add_route(app, fn)
