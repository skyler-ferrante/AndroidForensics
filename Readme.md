ADB

Get messages from ADB
-	adb shell content query --uri content://sms/inbox

Get contact data
-	adb shell content query --uri content://com.android.contacts/data/postals

Pull data from /sdcard (Should contain photos)
-	adb pull /sdcard .
