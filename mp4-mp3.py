import moviepy.editor as mp
clip = mp.VideoFileClip(r"/home/user/Desktop/videoplayback.mp4")
clip.audio.write_audiofile("movie_audio.mp3")
