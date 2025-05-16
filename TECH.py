import flet as ft
import random

def main(page: ft.Page):
    #states false STATE
    current_index = 0
    songon = False
    shuffle_mode = False
    repeat_mode = False
    is_muted = False
    current_playlist = 1

    playlists = {
        1: [1, 2, 3, 4, 5],
        2: [6, 7, 8, 9, 10],
        3: [11, 12, 13, 14, 15],
    }
    playlist = playlists[current_playlist].copy()

    audios = {
        1: ft.Audio(src="audios/Foo Fighters - Everlong (Official HD Video).mp3"),
        2: ft.Audio(src="audios/Goo Goo Dolls – Iris [Official Music Video] [4K Remaster].mp3"),
        3: ft.Audio(src="audios/Nirvana - Drain You (Audio).mp3"),
        4: ft.Audio(src="audios/Radiohead - Creep.mp3"),
        5: ft.Audio(src="audios/You're All I Want - Cigarettes After Sex.mp3"),

        6: ft.Audio(src="audios/Chevelle - Comfortable Liar (Official Audio).mp3"),
        7: ft.Audio(src="audios/Chevelle - The Red (Official HD Video).mp3"),
        8: ft.Audio(src="audios/Muse - Hysteria [Official Music Video].mp3"),
        9: ft.Audio(src="audios/Slipknot - Duality [OFFICIAL VIDEO] [HD].mp3"),
        10: ft.Audio(src="audios/System of a Down - Aerials (Remastered 2021).mp3"),
        
        11: ft.Audio(src="audios/The Strokes - Brooklyn Bridge to Chorus.mp3"),
        12: ft.Audio(src="audios/Eyedress & Dent May - Something About You.mp3"),
        13: ft.Audio(src="audios/HOMESHAKE  Love is Only a Feeling.mp3"),
        14: ft.Audio(src="audios/Mac DeMarco  One More Love Song (Official Audio).mp3"),
        15: ft.Audio(src="audios/Deftones - Rosemary (VisualLyrics).mp3"),
    }

    for audio in audios.values():
        page.overlay.append(audio)
#/////////////////////////////////////////////
    def chooseAudio():
        nonlocal current_index, songon
        song_id = playlist[current_index]

        for audio in audios.values():
            audio.pause()

        audios[song_id].play()
        img_map = {
            1: ("Everlong - Foo Fighters", "https://i1.sndcdn.com/artworks-pewMD4eo1wHAArvs-SEQCIQ-t500x500.jpg"),
            2: ("Iris - Goo Goo Dolls", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSxjmtBZpGBC7absKUwzAyx3JOZPHE27EpfoA&s"),
            3: ("Drain You - Nirvana", "https://upload.wikimedia.org/wikipedia/en/b/b7/NirvanaNevermindalbumcover.jpg"),
            4: ("Creep - Radiohead", "https://upload.wikimedia.org/wikipedia/en/0/0f/Radiohead.pablohoney.albumart.jpg"),
            5: ("You're all I want - Cigarettes After Sex", "https://f4.bcbits.com/img/a3109576526_65"),
            6: ("Comfortable Liar - Chevelle", "https://upload.wikimedia.org/wikipedia/en/5/5a/ChevelleWonderWhatsNext.jpg"),
            7: ("The Red - Chevelle", "https://upload.wikimedia.org/wikipedia/en/5/5a/ChevelleWonderWhatsNext.jpg"),
            8: ("Hysteria - Muse", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSRSw8II-3y0goszpoDEYq34L1i80juu8-9Jw&s"),
            9: ("Duality - Slipknot", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQZDKTLxZk3ALzy7Sh_QoYka4zH41wh6h0M-Q&s"),
            10: ("Aerials - System of a Down", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS0lEhsQRCFg935Vg24nl0x9xvhd4mwMXyubw&s"),
            11: ("Brooklyn Bridge to Chorus - The Strokes", "https://upload.wikimedia.org/wikipedia/en/f/f8/The_Strokes_-_The_New_Abnormal.png"),
            12: ("Something About You - Eyedress & Dent May", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRiqgSCnfrMSDpyLCGGjHshscnGXZzW_2cL_g&s"),
            13: ("Love is Only a Feeling - HOMESHAKE", "https://f4.bcbits.com/img/a2012758074_10.jpg"),
            14: ("One More Love Song - Mac Demarco", "https://i1.sndcdn.com/artworks-Lt7I60N8w30d-0-t500x500.jpg"),
            15: ("Rosemary - Deftones", "https://i1.sndcdn.com/artworks-0yk6BVtTOsrC-0-t1080x1080.jpg"),
        }

        cursong.value, img.src = img_map.get(song_id, ("Unknown", ""))

        songon = True
        playpause.text = "❚❚"
        page.update()
#/////////////////////////////////////////////
    def togglePlayPause(e):
        nonlocal songon
        song_id = playlist[current_index]
        if songon:
            audios[song_id].pause()
            playpause.text = "▶"
            songon = False
        else:
            audios[song_id].resume()
            playpause.text = "❚❚"
            songon = True
        page.update()

    def volumeChange(e):
        volume = volumeSlider.value
        for audio in audios.values():
            audio.volume = volume
        if volume <= 0:
            volumeIcon.text = "🔇"
        elif volume <= 0.5:
            volumeIcon.text = "🔈"
        elif volume <= 1.5:
            volumeIcon.text = "🔉"
        else:
            volumeIcon.text = "🔊"
        page.update()
#/////////////////////////////////////////////
    def Muting(e):
        nonlocal is_muted
        if is_muted:
            volumeSlider.value = 1.0
            is_muted = False
        else:
            volumeSlider.value = 0.0
            is_muted = True
        volumeChange(None)
        page.update()
#/////////////////////////////////////////////
    def nextSong(e):
        nonlocal current_index
        current_index = (current_index + 1) % len(playlist)
        chooseAudio()

    def previousSong(e):
        nonlocal current_index
        current_index = (current_index - 1) % len(playlist)
        chooseAudio()
#/////////////////////////////////////////////
    def toggleShuffle(e):
        nonlocal shuffle_mode, playlist, current_index
        shuffle_mode = not shuffle_mode
        if shuffle_mode:
            playlist = playlists[current_playlist].copy()
            random.shuffle(playlist)
            shuffleButton.color = ft.Colors.GREEN
        else:
            playlist = playlists[current_playlist].copy()
            shuffleButton.color = ft.Colors.WHITE
        current_index = 0
        chooseAudio()

    def toggleRepeat(e):
        nonlocal repeat_mode
        repeat_mode = not repeat_mode
        repeatButton.color = ft.Colors.GREEN if repeat_mode else ft.Colors.WHITE
        page.update()

    def switchPlaylist(e):
        nonlocal current_playlist, playlist, current_index
        current_playlist = int(e.control.data)
        playlist = playlists[current_playlist].copy()
        if shuffle_mode:
            random.shuffle(playlist)
        current_index = 0
        chooseAudio()
#/////////////////////////////////////////////
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = ft.colors.BLACK
    page.title = "tARADOs"
    page.padding = 20
    img = ft.Image(src="", width=350, height=350)
    cursong = ft.Text("", size=40, color=ft.colors.WHITE)
#/////////////////////////////////////////////
    playpause = ft.ElevatedButton(text="▶", color=ft.colors.WHITE, on_click=togglePlayPause)
    nextButton = ft.ElevatedButton(text="↪", color=ft.colors.WHITE, on_click=nextSong)
    previousButton = ft.ElevatedButton(text="↩", color=ft.colors.WHITE, on_click=previousSong)
    shuffleButton = ft.ElevatedButton(text="⇄", color=ft.colors.WHITE, on_click=toggleShuffle)
    repeatButton = ft.ElevatedButton(text="↻", color=ft.colors.WHITE, on_click=toggleRepeat)

    volumeSlider = ft.Slider(min=0, max=1, value=1, on_change=volumeChange)
    volumeIcon = ft.ElevatedButton(text="🔊", on_click=Muting, bgcolor=ft.colors.TRANSPARENT, color=ft.colors.WHITE, height=40, width=40)
#/////////////////////////////////////////////
    playlistButtons = ft.Column([
        ft.ElevatedButton(text="📁-Favs", data="1", on_click=switchPlaylist, bgcolor=ft.colors.TRANSPARENT),
        ft.ElevatedButton(text="📁-Steal", data="2", on_click=switchPlaylist, bgcolor=ft.colors.TRANSPARENT),
        ft.ElevatedButton(text="📁-RR", data="3", on_click=switchPlaylist, bgcolor=ft.colors.TRANSPARENT),
    ], alignment=ft.MainAxisAlignment.START)

    buttons = ft.Row([shuffleButton, previousButton, playpause, nextButton, repeatButton],
                     alignment=ft.MainAxisAlignment.CENTER, width=400)

    volumeArea = ft.Row([volumeIcon, volumeSlider], alignment=ft.MainAxisAlignment.START)
#/////////////////////////////////////////////
    page.add(
        img, cursong,
        buttons,
        ft.Column([playlistButtons, volumeArea], alignment=ft.MainAxisAlignment.START)
    )

    page.update()
    chooseAudio()

ft.app(target=main)
