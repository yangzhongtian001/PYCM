# -*- mode: python -*-

block_cipher = None


a = Analysis(['Main.py'],
             pathex=['E:\\Proj\\PYCM\\Client'],
             binaries=[],
             datas=[],
             hiddenimports=['PyQt5.sip'],
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
          [],
          exclude_binaries=True,
          name='PYCM-Client',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          console=False,
          icon='UI/Resources/logo.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               name='PYCM-Client')
app = BUNDLE(exe,
             name='PYCM-Client',
             icon='UI/Resources/logo.ico',
             bundle_identifier='io.hcc.pycm.client',
             info_plist={
                'NSHighResolutionCapable': 'True'
             })