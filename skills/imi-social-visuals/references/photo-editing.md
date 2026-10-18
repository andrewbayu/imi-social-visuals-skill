# Editing a real IMI photograph

1. Inspect the source photo. Identify the vessel, location, people, visible identifiers, and any part the user wants preserved or changed. Keep an untouched original.
2. Read the installed `imagegen` skill and use its edit workflow. Pass the actual source image as the **edit target**. Pass `assets/style-anchor-speedboat.png` only as a **color/editing style reference** if needed. State the roles explicitly in the prompt.
3. Request the approved muted olive/teal-charcoal grade, soft contrast, controlled warm highlights, haze where physically plausible, and selective depth. Use motion blur only if the captured action supports it; keep the vessel sharp and identifiable. A stationary boat must not acquire a high-speed wake.
4. Preserve real vessel geometry, hull color and markings, registration text, people, recognizable landmarks, and factual location unless the user asks to change them. Avoid inventing a new setting, weather event, vessel equipment, crew, or performance story. If the edit cannot preserve a critical detail, revert or use the original photo with conservative color correction.
5. Compose branding and copy with `scripts/compose.py` after editing so the exact logo and Montserrat/Inter are retained. Omit `Ilustrasi konsep` for a genuine, verified photograph; disclose material generative alterations when they would make the photo misleading.

For alternate ratios, inspect each crop. Generate or edit a new frame when a square or Story crop hides the vessel, action, or important identifiers.
