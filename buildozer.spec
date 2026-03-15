[app]

# 应用名称
title = 美墨签到

# 包名
package.name = meimosign
package.domain = com.qiqi

# 源代码目录
source.dir = .
source.include_exts = py,json,txt

# 版本号
version = 1.0.0

# 依赖 - 全部加上
requirements = python3,kivy,requests,urllib3,certifi,charset-normalizer,idna

# Android 配置
android.permissions = android.permission.INTERNET, android.permission.WRITE_EXTERNAL_STORAGE, android.permission.READ_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a

# 屏幕方向
orientation = portrait
fullscreen = 0

# Android 特定
android.accept_sdk_license = True
android.encoding = utf-8
android.release_artifact = apk

# Android 10+ 兼容
android.manifest.application.android:requestLegacyExternalStorage = true

[buildozer]
log_level = 2
warn_on_root = 0
