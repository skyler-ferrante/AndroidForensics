ADB commands for Android Forensics (Not root required)

Get messages from ADB
-	adb shell content query --uri content://sms/inbox

Get contact data
-	adb shell content query --uri content://com.android.contacts/data/postals

Pull data from /sdcard (Should contain photos)
-	adb pull /sdcard .

Make a backup
-	adb backup -all

[Extract Android Backup](https://stackoverflow.com/questions/18533567/how-to-extract-or-unpack-an-ab-file-android-backup-file)
-	adb backup -all
-	( printf "\x1f\x8b\x08\x00\x00\x00\x00\x00" ; tail -c +25 backup.ab ) |  tar xfvz -

To see SMS messages
-	cd apps/com.android.providers.telephony/d_f/
-	zlib-flate -uncompress < 000000_sms_backup
