# These and other macros are documented in dhd/droid-hal-device.inc
# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define device miatoll
%define vendor xiaomi

%define vendor_pretty Xiaomi
%define device_pretty Redmi Note 9 Pro

%define rpm_device miatoll

%define enable_kernel_update 1
%define enable_dtbo_update 1

%define droid_target_aarch64 1

%define straggler_files \
   /bugreports \
   /d \
   /sdcard \
%{nil}

# Using droid-system instead of mounting
%define makefstab_skip_entries /product /system /system_ext /vendor /dev/binderfs /metadata
Requires: droid-system

%include rpm/dhd/droid-hal-device.inc

# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"

