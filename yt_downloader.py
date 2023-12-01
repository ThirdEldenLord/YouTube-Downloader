from pytube import YouTube

link = input('Please paste a link for a video you want to download: ')

def downloader(link):
    video = YouTube(link)
    title = video.title
    dw_video = video.streams.get_highest_resolution()
    try:
        dw_video.download('D:\Загрузка')
        print(f'{title} was successfully download!')
    except:
        print('We get some error')
        
downloader(link)        