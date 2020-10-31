class Translation(object):
   START_TEXT = """<i>Vanakkam</i> <i><b>{}</b></i>,

Welcome to Our <a href='https://t.me/turboremaxbot'><b>Turbo Renamer ⚡</b></a> bot

I Can rename ✍ with custom thumbnail and upload as video/file

Type /help for more details."""
RENAME_403_ERR = "Sorry. You are not permitted to rename this file."
FORMAT_SELECTION = "Select the desired format: <a href='{}'>file size might be approximate</a> \nIf you want to set custom thumbnail, send photo before or quickly after tapping on any of the below buttons.\nYou can use /deletethumbnail to delete the auto-generated thumbnail."
SET_CUSTOM_USERNAME_PASSWORD = """If you want to download premium videos, provide in the following format: URL | filename | username | password"""
NOYES_URL = "@robot URL detected. Please use https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
RCHD_BOT_API_LIMIT = "size greater than maximum allowed size (50MB). Neverthless, trying to upload."
RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 1.5GB due to Telegram API limitations."
    #AFTER_SUCCESSFUL_UPLOAD_MSG = "Please rate me if you find me useful. Join : @SerialCoIn"
    #AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Downloaded in {} seconds. \nJoin : @SerialCoIn \nUploaded in {} seconds."
    #RENAME_403_ERR = "Sorry. You are not permitted to rename this file."
ABS_TEXT = " Please don't be selfish."
UPGRADE_TEXT = "There is no upgrade plan till now it will be added in future"
DOWNLOAD_START_VIDEO = "Downloading.....⤵️"
DOWNLOAD_START = "Downloading.....⤵️"
UPLOAD_START_VIDEO = "Uploading.....⤴️"
UPLOAD_START = "Uploading.....⤴️"
RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 1.5GB due to Telegram API limitations.I can't do anything for that 🤷‍♂️."
AFTER_SUCCESSFUL_UPLOAD_MSG = "**Thank you for Using [Turbo Renamer](https://t.me/JAsuran123)'s bot.**"
AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Downloaded in {} seconds.\nUploaded in {} seconds."
NOT_AUTH_USER_TEXT = "Please /upgrade your subscription."
NOT_AUTH_USER_TEXT_FILE_SIZE = "Detected File Size: {}. Free Users can only upload: {}\nPlease /upgrade your subscription.\nIf you think this is a bug, please contact <a href='https://t.me/JAsuran123'>Turbo Renamer</a>"
SAVED_CUSTOM_THUMB_NAIL = "Custom File thumbnail saved 🤗 permanently. This image will be used in the File."
DEL_ETED_CUSTOM_THUMB_NAIL = "🤔 Custom thumbnail cleared succesfully."
FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "🤨 Media cleared succesfully."
SAVED_RECVD_DOC_FILE = "👹 Document Downloaded Successfully."
CUSTOM_CAPTION_UL_FILE = "<b>\nShare and Support \n\n@SerialCoIn</b>"
NO_CUSTOM_THUMB_NAIL_FOUND = "😠 No Custom ThumbNail found."
NO_VOID_FORMAT_FOUND = "ERROR...\n<b>YouTubeDL</b> said: {}"
USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
HELP_USER = """Vanakkam <b><i>{}</i></b>, 

I am Turbo Renamer bot ✍ by <a href='https://t.me/JAsuran123'><b>Asuran</b></a>
    
1. Send Me A Thumbnail.

2. Send me the file to be Renamed.

3. Reply to that message with <code>/rename new name.extension</code>. with custom thumbnail support.\n(upload as file)

4. Reply to that message with <code>/renamev new name.extension</code>. with custom thumbnail support.\n(uploading as Video)

5. Reply to that message with <code>/gshoot</code> Uploading as Screenshots
   
<b>Thanks to <i><a href="https://t.me/JAsuran123">Turbo Renamer 🙇</a></i> for his source code. check /about for source code</b>

--------

Support Group : <b>@SerialCoIn</b>"""
AFTER_GET_DL_LINK = "Direct Link <a href='{}'>Generated</a> valid for {} days.\n© @SerialCoIn"
REPLY_TO_DOC_GET_LINK = "Reply to a Telegram media to get High Speed Direct Download Link"
REPLY_TO_DOC_FOR_RENAME_FILE = "🙆 Reply to a Telegram media to `/rename New Name.extension` with custom thumbnail support.\n\n(For uploading as file).\n\nSee /help for mor information. "
REPLY_TO_DOC_FOR_RENAME_VIDEO = "🙋 Reply to a Telegram media to `/rename_video New Name.extension` with custom thumbnail support.\n\n(For uploading as video).\n\nSee /help for mor information."
REPLY_TO_DOC_GET_LINK = "Reply to a Telegram media to get High Speed Direct Download Link"
REPLY_TO_DOC_FOR_C2V = "Reply to a Telegram media to convert"
REPLY_TO_DOC_FOR_SCSS = "Reply to /gshoot a Telegram Files to get screenshots"
REPLY_TO_DOC_FOR_RENAME_FILE = "Reply to a Telegram Files to /rename with custom thumbnail support"
AFTER_GET_DL_LINK = "Direct Link <a href='{}'>Generated</a> valid for {} days.\n @SerialCoIn"
FF_MPEG_RO_BOT_RE_SURRECT_ED = """Syntax: /trim HH:MM:SS [HH:MM:SS]"""
FF_MPEG_RO_BOT_STEP_TWO_TO_ONE = "First send /downloadmedia to any media so that it can be downloaded to my local. \nSend /storageinfo to know the media, that is currently downloaded."
FF_MPEG_RO_BOT_STOR_AGE_INFO = "Video Duration: {}\nSend /clearffmpegmedia to delete this media, from my storage.\nSend /trim HH:MM:SS [HH:MM:SS] to cu[l]t a small photo / video, from the above media."
FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "A saved media already exists. Please send /storageinfo to know the current media details."
USER_DELETED_FROM_DB = "User <a href='tg://user?id={}'>{}</a> deleted from DataBase."
REPLY_TO_DOC_OR_LINK_FOR_RARX_SRT = "Reply to a Telegram media (MKV), to extract embedded streams"
REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "Reply /generatecustomthumbnail to a media album, to generate custom thumbail"
ERR_ONLY_TWO_MEDIA_IN_ALBUM = "Media Album should contain only two photos. Please re-send the media album, and then try again, or send only two photos in an album."
INVALID_UPLOAD_BOT_URL_FORMAT = "URL format is incorrect. make sure your url starts with either http:// or https://. You can set custom file name using the format link | file_name.extension"
ABUSIVE_USERS = "You are not allowed to use this bot. If you think this is a mistake, please check /me to remove this restriction."
FF_MPEG_RO_BOT_AD_VER_TISE_MENT = "https://telegram.dog/CyberBoyAyush"
EXTRACT_ZIP_INTRO_ONE = "Send a compressed file first, Then reply /unzip command to the file."
EXTRACT_ZIP_INTRO_THREE = "Analyzing received file. ⚠️ This might take some time. Please be patient. "
UNZIP_SUPPORTED_EXTENSIONS = ("zip", "rar")
EXTRACT_ZIP_ERRS_OCCURED = "Sorry. Errors occurred while processing compressed file. Please check everything again twice, and if the issue persists, report this to @SerialCoIn"
EXTRACT_ZIP_STEP_TWO = """Select file_name to upload from the below options.
You can use /rename command after receiving file to rename it with custom thumbnail support."""
CANCEL_STR = "Process Cancelled"
ZIP_UPLOADED_STR = "Uploaded {} files in {} seconds"
FREE_USER_LIMIT_Q_SZE = """Cannot Process.
Free users only 1 request per 30 minutes.
/upgrade or Try 1800 seconds later."""
IFLONG_FILE_NAME = """File Name limit allowed by Telegram is {alimit} characters.
The given file name has {num} characters.

<b>Essays Not allowed in Telegram file name!</b>
©️ <code>@turboremaxbot</code>
Please short your file name and try again!"""

About = """Hi __{}__,\n
**📝 Language:** Python 3

**🧰 Framework:** Pyrogram

**👨‍💻 Developer:** [Turbo Renamer](https://t.me/Ns_AnoNymouS)

📮 Channel: [Serial](https://t.me/SerialCoIn)

**👥 Group:** [Tamil Serial Group](https://t.me/SerialCoIng)

**💻 Source Code:**[Press Me](https://github.com/AsuranJ/Turbo-Renamer)"""
