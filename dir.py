os.makedirs('/content/spectrograms3sec')
os.makedirs('/content/spectrograms3sec/train')
os.makedirs('/content/spectrograms3sec/test')

genres = 'blues classical country disco pop hiphop metal reggae rock'
genres = genres.split()
for g in genres:
  path_audio = os.path.join('/content/audio3sec',f'{g}')
  os.makedirs(path_audio)
  path_train = os.path.join('/content/gdrive/My Drive/spectrograms3sec/train',f'{g}')
  path_test = os.path.join('/content/gdrive/My Drive/spectrograms3sec/test',f'{g}')
  os. makedirs(path_train)
  os. makedirs(path_test)