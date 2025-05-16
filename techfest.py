import flet as ft
import random
 
def main(page: ft.Page):
    current_index = 0
    songon = False
    shuffle_mode = False
    repeat_mode = False
    playlist = [1, 2, 3, 4, 5]
 
#/////////////////////////////////////////////
    def chooseAudio():
        nonlocal current_index, songon
        song_id = playlist[current_index]
 
        audio1.pause()
        audio2.pause()
        audio3.pause()
        audio4.pause()
        audio5.pause()
 
        if repeat_mode == True:
            pass
        else:
            pass
 
        if song_id == 1:
            audio1.play()
            cursong.value = "Everlong - Foo Fighters"
            img.src = "https://i1.sndcdn.com/artworks-pewMD4eo1wHAArvs-SEQCIQ-t500x500.jpg"
        elif song_id == 2:
            audio2.play()
            cursong.value = "Iris - Goo Goo Dolls"
            img.src = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSxjmtBZpGBC7absKUwzAyx3JOZPHE27EpfoA&s"
        elif song_id == 3:
            audio3.play()
            cursong.value = "Drain You - Nirvana"
            img.src = "https://upload.wikimedia.org/wikipedia/en/b/b7/NirvanaNevermindalbumcover.jpg"
        elif song_id == 4:
            audio4.play()
            cursong.value = "Creep - Radiohead"
            img.src = "https://upload.wikimedia.org/wikipedia/en/0/0f/Radiohead.pablohoney.albumart.jpg"
        elif song_id == 5:
            audio5.play()
            cursong.value = "You're all I want - Cigarettes After Sex"
            img.src = "https://f4.bcbits.com/img/a3109576526_65"
 
        songon = True
        playpause.text = "| |"
        page.update()
#/////////////////////////////////////////////
    def nextSong(e):
        nonlocal current_index
        current_index += 1
        if current_index >= len(playlist):
            current_index = 0
        chooseAudio()
#/////////////////////////////////////////////
    def previousSong(e):
        nonlocal current_index
        current_index -= 1
        if current_index < 0:
            current_index = len(playlist) - 1
        chooseAudio()
#/////////////////////////////////////////////
    def togglePlayPause(e):
        nonlocal songon
        song_id = playlist[current_index]
        if songon:
            # Pause the song
            if song_id == 1:
                audio1.pause()
            elif song_id == 2:
                audio2.pause()
            elif song_id == 3:
                audio3.pause()
            elif song_id == 4:
                audio4.pause()
            elif song_id == 5:
                audio5.pause()
            songon = False
            playpause.text = "▶"
        else:
            # Resume the song from where it was paused
            if song_id == 1:
                audio1.resume()
            elif song_id == 2:
                audio2.resume()
            elif song_id == 3:
                audio3.resume()
            elif song_id == 4:
                audio4.resume()
            elif song_id == 5:
                audio5.resume()
            songon = True
            playpause.text = "| |"
       
        page.update()
#/////////////////////////////////////////////

    def volumeChange(e):
        pass

#/////////////////////////////////////////////

    def toggleShuffle(e):
        nonlocal shuffle_mode, playlist, current_index
        shuffle_mode = not shuffle_mode
        if shuffle_mode:
            random.shuffle(playlist)
            shuffleButton.color = ft.Colors.GREEN
        else:
            playlist = [1, 2, 3, 4, 5]
            shuffleButton.color = ft.Colors.WHITE
        current_index = 0
        chooseAudio()
 
    def toggleRepeat(e):
        nonlocal repeat_mode
        repeat_mode = not repeat_mode
        if repeat_mode:
            repeatButton.color = ft.Colors.GREEN
        else:
            repeatButton.color = ft.Colors.WHITE
        page.update()
 
#/////////////////////////////////////////////
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment  = ft.MainAxisAlignment.CENTER
    page.bgcolor = ft.colors.BLACK
#/////////////////////////////////////////////
    img = ft.Image(src="", width=350, height=350)
    cursong = ft.Text("", size=40, color=ft.Colors.WHITE)
    playpause = ft.ElevatedButton(text="Play", color=ft.Colors.WHITE, on_click=togglePlayPause)
    nextButton = ft.ElevatedButton(text="↪", color=ft.Colors.WHITE, on_click=nextSong)
    previousButton = ft.ElevatedButton(text="↩", color=ft.Colors.WHITE, on_click=previousSong)
    shuffleButton = ft.ElevatedButton(text="⇄ ", color=ft.Colors.WHITE, on_click=toggleShuffle)
    repeatButton = ft.ElevatedButton(text="↻", color = ft.Colors.WHITE, on_click=toggleRepeat)
    # volumeSlider = ft.Slider(min=0, max=1, value=, on_change=volumeChange)
#/////////////////////////////////////////////
    audio1 = ft.Audio(src="audios/Foo Fighters - Everlong (Official HD Video).mp3")
    audio2 = ft.Audio(src="audios/Goo Goo Dolls – Iris [Official Music Video] [4K Remaster].mp3")
    audio3 = ft.Audio(src="audios/Nirvana - Drain You (Audio).mp3")
    audio4 = ft.Audio(src="audios/Radiohead - Creep.mp3")
    audio5 = ft.Audio(src="audios/You're All I Want - Cigarettes After Sex.mp3")
 
    page.overlay.append(audio1)
    page.overlay.append(audio2)
    page.overlay.append(audio3)
    page.overlay.append(audio4)
    page.overlay.append(audio5)
#/////////////////////////////////////////////
    buttons = ft.Row(
        controls=[shuffleButton, previousButton, playpause, nextButton, repeatButton],
        alignment=ft.MainAxisAlignment.CENTER,
        width=400,
    )
 
 
    page.add(img, cursong, buttons)
    page.update()
    chooseAudio()
 
ft.app(target=main)