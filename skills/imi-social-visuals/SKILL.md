---
name: imi-social-visuals
description: Create consistent Inovasi Maritim social post artwork or restyle real vessel photos for 1080x1350, 1080x1920, and 1080x1080 formats. Use when making IMI feed, Story, or square visuals with the approved logo, typography, image treatment, and layout.
---

# IMI Social Visuals

Produce an IMI visual whose **scene serves the post idea** and whose image treatment, logo, type, and spacing match the approved direction. This skill covers new conceptual visuals and edits to the team's own photographs. It does not authorize posting or claiming that a generated vessel is a real IMI project.

## Visual rules

- Choose vessel type, action, and setting from the post's message. The approved photographic treatment is portable: muted olive/teal and charcoal grade, subdued highlights, filmic contrast, gentle haze, selective depth of field, and motion blur when movement warrants it. **The reference's industrial harbor is not a required setting.** See [visual-direction.md](references/visual-direction.md) for reference roles and scene examples, and [composition.md](references/composition.md) for the composition principles learned from the supplied video.
- Put the actual white transparent IMI logo at the top left, approximately 80 px from both edges, on a background with enough contrast. The bundled logo is `assets/imi-logo-white.png`; do not ask image generation to redraw it.
- Set headlines and subheadlines in the bundled Montserrat font, and body/footer text in Inter. Keep 25 px of clear space between the final headline line and subheadline. Put the headline block near the bottom over a soft dark fade; center the website in the footer. Do not add blueprint or technical drawing lines.
- Use exact target dimensions: `1080x1350` feed portrait, `1080x1920` Story/Reel cover, or `1080x1080` square. For Story, allow extra bottom space for platform UI. Keep the vessel and key action visible after cropping.
- Use concise Indonesian copy grounded in IMI's actual products and services. Do not invent performance, delivery, certification, price, or project claims. Label generated scenes `Ilustrasi konsep`; do not label verified real photos this way.

## Create or edit the background

For a new conceptual scene, use the installed `imagegen` skill and its built-in tool. Specify the intended vessel and action, a distinct scene appropriate to the message, and the photographic treatment separately. Plan a single visual hierarchy and the text-safe region using [composition.md](references/composition.md). Use supplied vessel images as **geometry references** and the bundled `assets/style-anchor-speedboat.png` as **treatment reference only** when useful; neither should force the next scene to show the same boat or islands. Generate a clean background without text, brand marks, or drafting graphics. Save selected project images to the project workspace.

For a real team photo, read [photo-editing.md](references/photo-editing.md) and use the installed `imagegen` skill's edit path. Preserve the actual vessel's identity, shape, markings, people, and scene unless the user requests a specific change. Apply grade, light, atmosphere, and motion treatment without fabricating a new boat or new location. Inspect the original with `view_image` before editing and inspect the result before use.

## Compose and review

Use `scripts/compose.py` to place the actual logo and exact fonts on the selected background. It supports all three target sizes, headline lines, a subheadline, a footer URL, a concept label, and a focal point for cropping. Run `python3 scripts/compose.py --help` for arguments. Use a separate background for a format when its crop loses the subject; do not force one photograph through every ratio.

Inspect every finished output at full size and at phone size: logo legibility, vessel silhouette, clear visual path toward the subject, headline/subheadline gap, text spelling, bottom safe area, and absence of incidental fake labels or technical marks. Revise only visible defects. Save the source background, final artwork, and concise caption or prompt record in the requested project folder. Provide the completed file paths.
