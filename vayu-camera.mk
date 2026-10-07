# SPDX-License-Identifier: Apache-2.0

# Permissions
PRODUCT_COPY_FILES += \
    vendor/xiaomi/vayu-camera/configs/default-permissions/miuicamera-permissions.xml:$(TARGET_COPY_OUT_SYSTEM)/etc/default-permissions/miuicamera-permissions.xml \
    vendor/xiaomi/vayu-camera/configs/permissions/privapp-permissions-miuicamera.xml:$(TARGET_COPY_OUT_SYSTEM)/etc/permissions/privapp-permissions-miuicamera.xml \
    vendor/xiaomi/vayu-camera/configs/sysconfig/miuicamera-hiddenapi-package-whitelist.xml:$(TARGET_COPY_OUT_SYSTEM)/etc/sysconfig/miuicamera-hiddenapi-package-whitelist.xml

# Shims
PRODUCT_PACKAGES += \
    libgui_shim_miuicamera \
    MiuiSecurityCenterCta

# Props
PRODUCT_PRODUCT_PROPERTIES += \
    ro.hardware.camera=xiaomi \
    ro.com.google.lens.oem_camera_package=com.android.camera

PRODUCT_SYSTEM_PROPERTIES += \
    ro.miui.notch=1 \
    ro.product.mod_device=vayu

PRODUCT_VENDOR_PROPERTIES += \
    persist.vendor.camera.privapp.list=com.android.camera \
    vendor.vidhance.enabled=0 \
    vendor.vidhance.video.enabled=0 \
    vendor.vidhance.preview.enabled=0 \
    arm64.memtag.process.android.hardware.camera.provider@2.4-service_64=off

# Inherit from vendor
$(call inherit-product, vendor/xiaomi/vayu-camera/common/vayu-camera-vendor.mk)
