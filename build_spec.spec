# build_spec.spec

# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(['presenter.py', 'model.py', 'viewer.py'],  # Укажите файл(ы) с вашим кодом
             pathex=['/Users/hfast/Desktop/my_repo'],  # Укажите путь к папке с вашим кодом
             binaries=[],
             datas=[('config.ini', '.'), ('calculator.png', '.')],  # Укажите файлы, которые нужно включить в сборку
             hiddenimports=['model', 'viewer', 'config'],  # Укажите импорты, которые не были найдены автоматически
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
          cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='MyCalc',  # Укажите имя исполняемого файла
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          upx_include=[],
          runtime_tmpdir=None,
          console=True )
