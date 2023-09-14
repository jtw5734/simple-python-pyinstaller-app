# extra-hooks/hooks-uvicorn.py
from PyInstaller.utils.hooks import collect_submodules

hiddenimports = collect_submodules('uvicorn')
hiddenimports = collect_submodules('logging')

hiddenimports = collect_submodules('config')
hiddenimports = collect_submodules('modules')
hiddenimports = collect_submodules('logging')

hiddenimports = collect_submodules('router')
hiddenimports = collect_submodules('routers.users')
hiddenimports = collect_submodules('routers.utils')
hiddenimports = collect_submodules('routers.install')
hiddenimports = collect_submodules('routers.router_collect')

hiddenimports = collect_submodules('handler')
hiddenimports = collect_submodules('model')