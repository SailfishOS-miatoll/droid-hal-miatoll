# These and other macros are documented in dhd/droid-hal-device.inc
# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define device miatoll
%define vendor xiaomi

%define vendor_pretty Xiaomi
%define device_pretty Redmi Note 9 Pro

%define rpm_device miatoll

%define enable_kernel_update 1
%define enable_dtbo_update 1

# want adreno quirks is required for browser at least, and other subtle issues
%define android_config \
#define WANT_ADRENO_QUIRKS 1\
%{nil}

%define droid_target_aarch64 1

%define straggler_files \
   /bugreports \
   /d \
   /sdcard \
%{nil}

# Using droid-system instead of mounting
%define makefstab_skip_entries /product /system /system_ext /vendor /dev/binderfs /metadata /vendor/dsp /vendor/bt_firmware /vendor/firmware_mnt
Requires: droid-system

%include rpm/dhd/droid-hal-device.inc

# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"

