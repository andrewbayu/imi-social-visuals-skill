# IMI Social Visuals

Reusable Codex skill for Inovasi Maritim social artwork and photo restyling in 1080×1350, 1080×1920, and 1080×1080. It includes the approved logo, licensed Montserrat and Inter fonts, photographic references, composition guidance, and a deterministic layout script.

## Install

Team members need access to the private `andrewbayu/imi-social-visuals-skill` GitHub repository. Install with Codex's `skill-installer`:

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo andrewbayu/imi-social-visuals-skill \
  --path skills/imi-social-visuals
```

Restart Codex or start a new conversation after installation. Invoke `$imi-social-visuals` with the post idea, format, copy, and any actual vessel or photo references. For example: “Use `$imi-social-visuals` to make a 1080x1350 post about a crew boat crossing open island water.”

The installer uses existing GitHub credentials for private repositories. To install into a project instead of the personal skills folder, add `--dest /absolute/path/to/project/.agents/skills`.

## Image composition dependency

`scripts/compose.py` needs Python 3 and Pillow (`python3 -m pip install Pillow`). It adds the bundled logo and fonts after the background image is prepared. Image creation and photo editing use the available `imagegen` skill and tool; this repository does not include a separate image-generation service or credentials.

```bash
python3 ~/.codex/skills/imi-social-visuals/scripts/compose.py \
  --image /absolute/path/to/background.png \
  --format 1080x1350 \
  --headline-line 'Kapal Anda.' \
  --headline-line 'Misi Anda.' \
  --subheadline 'Solusi kapal sesuai kebutuhan' \
  --source-type concept \
  --output /absolute/path/to/post.png
```

Use `--source-type photo` for verified real photos. Read [SKILL.md](SKILL.md) for the visual rules and factuality checks. Do not use generated scenes to imply an actual IMI delivery or project.
