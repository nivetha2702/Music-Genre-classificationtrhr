for g in genres:
  j = 0
  print(g)
  for filename in os.listdir(os.path.join('/content/audio3sec',f"{g}")):
    song  =  os.path.join(f'/content/audio3sec/{g}',f'{filename}')
    j = j+1
    
    y,sr = librosa.load(song,duration=3)
    #print(sr)
    mels = librosa.feature.melspectrogram(y=y,sr=sr)
    fig = plt.Figure()
    canvas = FigureCanvas(fig)
    p = plt.imshow(librosa.power_to_db(mels,ref=np.max))
    plt.savefig(f'/content/gdrive/My Drive/spectrograms3sec/{g}/{g+str(j)}.png')