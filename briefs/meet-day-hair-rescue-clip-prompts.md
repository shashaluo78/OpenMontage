# Meet-Day Hair Rescue — Final Production Sheet

This replaces all earlier versions.

Vertical 9:16 · about 30 seconds · 6 video clips (3 story + 3 demos)

> **Update (fal.ai production):** Demo 7 is cut. All images are final (supplied by the user, saved in `projects/meet-day-hair-rescue/assets/images/`). The Demo 4 and Demo 6 prompts below were reworded to match the final start frames: Demo 4 uses her own hand, Demo 6 uses a stylist's gloved hands.

---

## PART 1 — Image checklist

### Already done (keep these)

| File | Status |
|---|---|
| `start.png` | ✅ keep |
| `brush.png` | ✅ keep |
| `demo4_before.png` / `demo4_after.png` | ✅ keep |
| `demo5_before.png` / `demo5_after.png` | ✅ keep |
| `demo6_before.png` / `demo6_after.png` | ✅ keep (the originals) |

### Still to make (5 images, in Gemini or ChatGPT)

| # | Save as | Upload these | Prompt |
|---|---|---|---|
| ~~1~~ | ~~`demo7_after.png`~~ (cut: Demo 7 dropped) | | |
| 2 | `demo4_start.png` | `demo4_before.png` + `brush.png` | **Prompt B** |
| 3 | `demo5_start.png` | `demo5_before.png` + `brush.png` | **Prompt B** |
| ~~4~~ | ~~`demo7_start.png`~~ (cut: Demo 7 dropped) | | |
| 5 | `demo6_start.png` | `demo6_before.png` + `brush.png` | **Prompt C** |

When uploading two images, upload the before/after image FIRST and `brush.png` SECOND.

**Prompt A** (fixes the outfit change in demo 7)
```
Edit this photo. Keep her orange sweater, the framing, the lighting and the background exactly the same. Do not add a cape and do not change any clothing. Remove the claw clip and make ALL of her hair perfectly sleek, straight and glossy, falling smoothly down her back over the orange sweater. Portrait 9:16.
```

**Prompt B** (stylist's hand from behind, used for demos 4, 5 and 7)
```
Edit the first photo. Keep the exact same framing as the original: do not zoom in or crop; the claw clip, her shoulders and the background must stay fully visible and unchanged. Add a stylist's hand wearing a black nitrile glove, coming in from the top right of the frame, wrist above the brush, holding the handle of the brush from the second image (same cream oval brush with silver-outlined back panel and yellow end cap) the normal way, like a paddle brush, fingers wrapped around the handle and thumb on top. The bristles press into her hair just under the claw clip at the centre, with the back of the brush facing the camera and the handle pointing up and to the right. Keep her hair, clothes, clip and background exactly the same. Portrait 9:16, photorealistic.
```

**Prompt C** (she brushes her own hair, side view, demo 6)
```
Edit the first photo. Keep the exact same framing as the original; do not zoom in or crop. Her own hand comes up from under the black salon cape, holding the brush from the second image (same cream oval brush with silver-outlined back panel and yellow end cap) the normal way, fingers wrapped around the handle, placed at the roots on the side of her hair nearest the camera, ready to brush down. Keep her face, hair, cape, lighting and background exactly the same. Portrait 9:16, photorealistic.
```

**Check every start image:**
- natural hand with five fingers
- same framing as the before image (nothing zoomed or cropped)
- the cream brush with the yellow cap

---

## PART 2 — Video checklist (Hailuo)

> **Update:** Clip 2 is cut. Clip 3 is the user's Hailuo render (start frame `clip2_start.jpg`, Clip 3 prompt below), watermark removed with ffmpeg delogo. Edit order: clip1 → clip3 → demo4 → demo5 → demo6.


Settings for every clip: **MiniMax H3** · **Start/End Frame** · **768p** · **5s** · aspect ratio **Auto**

| # | Save as | Start Frame | End Frame | Prompt |
|---|---|---|---|---|
| 1 | `clip1.mp4` | `start.png` | (empty) | **Clip 1** |
| 2 | `clip2.mp4` | `clip2_start.jpg` | `clip2_end.jpg` | **Clip 2** |
| 3 | `clip3.mp4` | `clip3_start.png` (last frame of clip2) | `clip3_end.jpg` | **Clip 3** |
| 4 | `demo4.mp4` | `demo4_start.png` | `demo4_after.png` | **Demo 4** |
| 5 | `demo5.mp4` | `demo5_start.png` | `demo5_after.png` | **Demo 5** |
| 6 | `demo6.mp4` | `demo6_start.png` | `demo6_after.png` | **Demo 6** |

To get a "last frame", play the clip to the very end, pause it and take a screenshot. Crop the screenshot to just the video.

**Clip 1**
```
Vertical handheld smartphone video, slight natural camera shake, eye-level medium shot. Indoor gymnastics competition hall with folding chairs, blue banners and people walking in the blurred background. The woman behind the seated girl works the black comb through the girl's frizzy, tangled brown hair, and the comb gets stuck in a tangle. The girl pouts, rolls her eyes and slumps impatiently in the chair, clearly bored of waiting. The woman tries again, then sighs and looks toward the camera helplessly. The man beside them watches with a small knowing smile. Realistic, candid, real-time speed, no text. Audio: natural indoor crowd ambience only, no speech, no music.
```

**Clip 2** (start frame: `clip2_start.jpg`, dad already holding the brush; end frame: `clip2_end.jpg`, one sleek stripe)
```
Vertical handheld smartphone video, eye-level medium shot. The camera holds the same distance for the whole clip: no zoom, no push-in, and all three faces stay fully in frame. Indoor gymnastics competition hall with blue banners and people walking in the blurred background, bright even overhead lighting. The girl sits on the black folding chair in her blue sparkly leotard, pink backpack and gold medal, with her lavender headband on her head. The lavender headband stays on her head and clearly visible for the entire clip. The man in the denim shirt holds the brush already resting on top of her head: a cream-coloured oval paddle brush whose back is smooth cream with a silver-outlined oval panel, a small round cream button and a silver oval ring, on a slim cream handle with a small yellow end cap. The brush head is entirely cream with no yellow on it. With a confident little smile he pulls the brush slowly down through the frizzy hair on his side, from the top of her head down past her shoulder, in one smooth stroke, holding it by the handle with the back of the brush facing the camera. Only the strip of hair the brush touches turns smooth, straight and glossy, leaving one clear sleek stripe about the width of the brush through the frizz. All the rest of her hair stays frizzy and tangled. The woman stops combing, lowers the comb and leans in slightly with her eyebrows raised in disbelief. The girl's wince relaxes and she glances sideways with curious wide eyes. Realistic, candid, real-time speed, no text. Audio: natural indoor crowd ambience only, no speech, no music.
```

**Clip 3** (8s; start frame: `clip3_start.png` = last frame of clip2; end frame: `clip3_end.jpg`). Three strokes; only the brush touches the hair.
```
Vertical handheld smartphone video, eye-level medium shot. Camera holds the same distance, no zoom; all three people stay fully in frame. Gymnastics hall, blue banners, blurred crowd, bright lighting. The girl sits on the black folding chair in her blue sparkly leotard, black sparkly leggings, pink backpack, gold medal and lavender headband; the headband stays on throughout. The woman in the green cardigan stands behind the chair on the left. The man in the denim shirt stands behind it on the right, holding the cream oval brush (silver-outlined back panel, slim handle, small yellow end cap) in his right hand. Rule: ONLY the brush bristles touch the girl's hair. No hand or finger touches her hair. The man's free left hand stays still at his side. The woman keeps both arms relaxed at her sides, comb motionless in her lowered hand, only watching wide-eyed. The man makes exactly three brush strokes, each straight down from the crown to the ends, and her hair hangs down naturally under gravity, never lifting or fanning out: Stroke 1: down the side of her hair nearest him, on the right of the frame. That side turns sleek and glossy; the rest stays frizzy. Stroke 2: down the back of her head. The top and back turn sleek; the left side is still frizzy. Stroke 3: he reaches his arm across in front of her face, without touching her face, and brushes down the side of her hair nearest the woman, on the left of the frame. Now all of her long brown hair is smooth, straight and glossy. Only after the third stroke: he lifts the brush away, holding it firmly by the handle, and raises it beside his face in a small proud wave, smiling. The woman covers her mouth with both hands in happy surprise. The girl grins hugely and hops up to stand in front of the chair, then lightly lifts one sleek lock with her fingertips to show it off. Realistic, candid, real-time speed, natural hair physics, no text. Audio: natural indoor crowd ambience only, no speech, no music.
```

**Demo 4** (her own hand; start `demo4_start.jpg`, end `demo4_after.png`)
```
Vertical close-up from behind, steady locked-off camera, no zoom; the framing stays exactly the same for the whole clip. Bright modern salon with mirrors and product shelves softly blurred, soft even lighting. A woman with thick, tightly coiled black natural hair sits with her back to the camera in a coral button-up shirt; the top section of her hair is held up in a black rectangular claw clip. She reaches back with her own right hand, in her coral sleeve, holding the cream oval brush (smooth cream back with a silver-outlined oval panel, small round button and silver oval ring, slim cream handle, small yellow end cap), with the back of the brush facing the camera. Rule: ONLY the brush bristles touch her hair. No finger or hand touches her hair. In one slow, smooth stroke she pulls the brush straight down from just under the claw clip, through the centre of her hair, to the ends at her neckline. The hair changes only where the bristles pass: a single stripe of hair about the width of the brush turns sleek, straight and glossy black, hanging flat, while the coils on both sides and the hair above the clip stay exactly as they are, full and springy. The clip never moves. At the end of the stroke she lowers her arm and the brush out of frame, leaving the sleek stripe down the centre of her coils. Realistic hair texture, satisfying, real-time speed, no text. Audio: soft brushing sound only, no speech, no music.
```

**Demo 5** (stylist's gloved hand; start `demo5_start.jpg`, end `demo5_after.png`)
```
Vertical close-up from behind, steady locked-off camera, no zoom; the framing stays the same for the whole clip. Warm modern salon softly blurred behind her, soft natural window light. A woman with long, dense, black corkscrew curls sits with her back to the camera in a rust-orange knit sweater; the top section of her hair is held in a black claw clip. A stylist's hand in a black nitrile glove enters from the top right, holding the cream oval brush by its slim cream handle (smooth cream back with a silver-outlined oval panel, small round button and silver oval ring, small yellow end cap), back of the brush facing the camera, bristles pressed into her hair just under the clip. Rule: ONLY the brush bristles touch her hair. No finger touches her hair. The stylist makes one slow, real brush stroke straight down the centre of her hair to the ends, with natural wrist movement and a little resistance as the bristles work through the curls. Real hair physics: the bristles catch the curls and gently pull them taut, and the hair directly behind the brush relaxes into straight, smooth strands. The sleek section looks like real blow-dried hair with visible individual strands and a soft natural sheen, not a plastic or painted band; its edges blend softly into the curls beside it. The stripe forms exactly where the bristles have just passed and nowhere else. The curls on both sides and the hair above the clip keep moving slightly and naturally but stay curly. The clip never moves. At the end of the stroke the hand lifts the brush away and out of frame, leaving one natural-looking straight section down the centre of her curls. Photorealistic, natural, satisfying, real-time speed, no text. Audio: soft natural brushing sound only, no speech, no music.
```

**Demo 6** (stylist's gloved hands)
```
Vertical three-quarter side view. A stylist's black-gloved hand slowly pulls the cream oval brush from the crown down the side of her hair nearest the camera to the ends, while the stylist's other gloved hand smooths the section. Only that section turns sleek, straight and glossy; the rest of her hair stays wavy. The stroke finishes with the brush near the ends of her hair. She stays seated and still, looking down calmly. Steady camera, soft salon lighting, realistic. Audio: soft brushing sound only, no speech, no music.
```

---

## PART 3 — Upload to GitHub when done

https://github.com/shashaluo78/OpenMontage/upload/claude/nice-keller-7yqfpa

Upload: `clip1.mp4` `clip2.mp4` `clip3.mp4` `demo4.mp4` `demo5.mp4` `demo6.mp4`

Final order in the edit: clip1 → clip3 → demo4 → demo5 → demo6
