from pytube import YouTube

url = input("ダウンロードしたい動画のURLは？　")
for i in YouTube(url).streams.all():
    print(i)
YouTube(url).streams.get_by_itag(int(input("どのtagにする？　"))).download()
print("ダウンロード完了！")
