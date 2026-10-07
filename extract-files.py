#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-License-Identifier: Apache-2.0
#

from os import path

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)
from extract_utils.tools import android_root

namespace_imports = [
    'vendor/xiaomi/vayu',
    'hardware/qcom-caf/sm8150',
]

blob_fixups: blob_fixups_user_type = {
    'system/lib64/libcamera_algoup_jni.xiaomi.so': blob_fixup()
        .add_needed('libgui_shim_miuicamera.so'),
    'system/lib64/libcamera_mianode_jni.xiaomi.so': blob_fixup()
        .add_needed('libgui_shim_miuicamera.so'),
    'system/lib64/libmicampostproc_client.so': blob_fixup()
        .remove_needed('libhidltransport.so'),
    'vendor/lib64/libcamera_dirty.so': blob_fixup()
        .sig_replace(
            'ff 03 02 d1 e9 23 02 6d f9 1b 00 f9 f8 5f 04 a9',
            '20008052440000b49f7c00a9c0035fd6',
        ),
    'vendor/lib64/libmialgoengine.so': blob_fixup()
        .sig_replace(
            '1f 11 00 71 e8 04 00 54 85 06 40 f9',
            '1f11007108030054850640f9',
        )
        .sig_replace(
            '1f 0d 00 71 08 02 00 54 85 06 40 f9',
            '1f0d007128000054850640f9',
        )
        .sig_replace(
            '85 06 40 f9 86 2e 40 b9 87 22 46 a9 89 2a 43 a9 21 ff ff f0 42 ff ff d0 83 ff ff 90 21 88 2f 91 42 8c 05 91 63 c0 3a 91 60 00 80 52 e4 59 80 52 e9 ab 00 a9 e8 03 00 f9 27 f6 00 94',
            '881a40b968d601b9881e40b968da01b90b0000141f2003d51f2003d51f2003d51f2003d51f2003d51f2003d51f2003d51f2003d51f2003d51f2003d5',
        ),
}  # fmt: skip

module = ExtractUtilsModule(
    'vayu-camera',
    'xiaomi',
    device_rel_path='vendor/xiaomi/vayu-camera',
    blob_fixups=blob_fixups,
    namespace_imports=namespace_imports,
)

module.vendor_rel_path = 'vendor/xiaomi/vayu-camera/common'
module.vendor_path = path.join(android_root, module.vendor_rel_path)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
