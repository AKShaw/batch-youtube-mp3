import youtube_dl
import sys, os

__author__ = "Alex Shaw"
__year__ = "2016"
__purpose__= "Download a whole list of youtube videos and convert them to MP3"


def get_link_array(file):
    """
    Intakes a file path, returns a list of strings with no line breaks

    :param file:
    :return: lines
    """
    try:
        with open(file) as f:
            lines = f.readlines()
            if len(lines) == 0:
                print("No links in file, aborting...")
                sys.exit()

            #strip \n from all strings in list
            for i in range(len(lines)):
                lines[i] = lines[i].strip("\n")

            return lines
    except IOError:
        print("Please select a valid file, aborting...")
        sys.exit()


def download_links_as_mp3(links, output_path):
    """
    Intakes a list of youtube links, downloads and converts to MP3

    :param links:
    :return: nothing
    """
    output = output_path + "\\%(title)s.%(ext)s"
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(links)


def main():
    """
    Gets the cl args, calls methods to convert them to a list and then downloads

    :return: nothing
    """
    try:
        #Gets file
        youtube_links_file = sys.argv[1]
        output_path = sys.argv[2]
        if os.path.exists(output_path)==False:
            try:
                os.mkdir(output_path)
            except PermissionError:
                print("Output path doesn't exist and program lacks permissions to create it. Please create manually and \
                try again.")
                sys.exit()

        #returns a list of strings without break characters
        youtube_links = get_link_array(youtube_links_file)
        download_links_as_mp3(youtube_links, output_path)
    except IndexError:
        print("usage: batch_download.py <full path to txt file with links> <full output path>")
        sys.exit()


main()
