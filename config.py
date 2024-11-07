# specify the paths to the image and JSON file
input_path = "google_photos/"
output_path = "output/"
reject_path = "reject/"

supportedMediaFileTypes = {
    '.jpeg': { "supportsExif": True },
    '.jpg' : { "supportsExif": True },
    '.heic': { "supportsExif": True },
    '.heif': { "supportsExif": True },
    '.webp': { "supportsExif": True },
    '.cr2': { "supportsExif": True },
    '.3gp': { "supportsExif": True },
    '.gif': { "supportsExif": True },
    '.mp4': { "supportsExif": True },
    '.png': { "supportsExif": True },
    '.avi': { "supportsExif": True },
    '.mov': { "supportsExif": True }
}

dry_run = False
verbose = True
