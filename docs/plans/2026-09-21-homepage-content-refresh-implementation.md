# Academic Homepage Content Refresh Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Complete Yudong Mu's academic homepage with an English-first home page, six accurate publication entries, a real Honors page, and restrained responsive styling.

**Architecture:** Keep the existing Jekyll/Academic Pages site and represent maintainable content in Markdown/front matter. Render publications through a dedicated include, keep project and honors presentation CSS in one small SCSS partial, and verify source structure plus a full Jekyll build.

**Tech Stack:** Jekyll, Liquid, Markdown, HTML5, SCSS, Python 3 standard library, GitHub Pages-compatible plugins.

---

### Task 1: Add source-level content verification

**Files:**
- Create: `scripts/verify_homepage_content.py`

**Step 1: Write the failing verification script**

Create a standard-library Python script that asserts:

- `_pages/about.md` contains `Selected Research Projects`, `FDHA`, `DFU-Y`, `GenCNN`, and `NFMap`, and does not present dLLM as a project.
- `_pages/honors.html` has `title: "Honors"`, `permalink: /honors/`, and the graduate and undergraduate awards from the approved CV.
- `_publications/` contains exactly six Markdown records and no starter/sample record.
- Publication sources contain GenCNN, the Chinese YOLO title, FDHA, NFMap, A2RT, and the RISC-V paper.
- `_pages/publications.html` uses `_includes/publication-entry.html`.
- `assets/css/main.scss` imports the new homepage styles.

**Step 2: Run it to verify it fails**

Run: `python scripts/verify_homepage_content.py`

Expected: FAIL because the current home page, Honors page, publication collection, include, and style import are incomplete.

**Step 3: Commit the failing check**

```bash
git add scripts/verify_homepage_content.py
git commit -m "test: add homepage content verification"
```

### Task 2: Refresh the home page

**Files:**
- Modify: `_pages/about.md`

**Step 1: Replace starter copy with the approved structure**

Add an English introduction, research interests, education, selected project cards, industry experience, and contact line. Use concise outcome-focused summaries:

- FDHA: cross-operator fusion and PE/TPE heterogeneous pipeline; 3.28x and 2.62x speedups.
- DFU-Y: YOLO-oriented mapping/fusion/double buffering; 2.527x performance and 2.658x energy-efficiency improvements.
- GenCNN: NSGA-II-based multi-objective mapping; 17.66x compilation and 6.47x execution speedups over AutoTVM.
- NFMap: network-flow-constrained node fusion; 1.43x mapping-quality and 1.14x compilation-speed improvements over E2EMap.

Keep dLLM out of the project section. Link project cards to their publication pages.

**Step 2: Run the focused check**

Run: `python scripts/verify_homepage_content.py`

Expected: Home-page assertions pass; the overall command still fails on unfinished publications, honors, and styles.

**Step 3: Commit**

```bash
git add _pages/about.md
git commit -m "feat: expand academic homepage content"
```

### Task 3: Rebuild the Publications page and records

**Files:**
- Create: `_includes/publication-entry.html`
- Modify: `_pages/publications.html`
- Delete: `_publications/2010-10-01-paper-title-number-2.md`
- Modify: `_publications/2025-01-YOLO.md`
- Modify: `_publications/2025-07-NFMap.md`
- Modify: `_publications/2025-08-FHDA.md`
- Modify: `_publications/2025-GenCNN.md`
- Create: `_publications/2025-RISCV-CNN.md`
- Create: `_publications/2026-A2RT.md`

**Step 1: Add the dedicated publication include**

Render a semantic `<article>` with title, author list, venue/year metadata, classification badges, concise summary, and DOI/paper buttons. Use Liquid conditionals so missing links do not render empty actions.

**Step 2: Update the Publications archive**

Keep the existing category loop but replace `archive-single.html` with `publication-entry.html`. Use `Journal Articles` and `Conference Papers` headings.

**Step 3: Normalize all six records**

Store complete author lists and official bibliographic metadata from the latest CV. Preserve `面向 YOLO 神经网络的数据流架构优化研究` and `《计算机学报》` in Chinese. Add verified DOI or publisher links where available, and remove all `To be added`, fake journal, MathJax demo, and Academic Pages placeholder content.

**Step 4: Run the focused check**

Run: `python scripts/verify_homepage_content.py`

Expected: Publication assertions pass; the overall command still fails on unfinished Honors and styles.

**Step 5: Commit**

```bash
git add _includes/publication-entry.html _pages/publications.html _publications
git commit -m "feat: complete publication archive"
```

### Task 4: Replace the placeholder Honors page

**Files:**
- Modify: `_pages/honors.html`
- Delete: `_honors/2012-03-01-talk-1.md`
- Delete: `_honors/2013-03-01-tutorial-1.md`
- Delete: `_honors/2014-02-01-talk-2.md`
- Delete: `_honors/2014-03-01-talk-3.md`

**Step 1: Correct page metadata and content**

Set the title to `Honors`, permalink to `/honors/`, and render a short introduction followed by dated Graduate and Undergraduate sections. Include every honor from the latest two-page CV, consolidating repeated undergraduate awards with counts.

**Step 2: Remove mislabeled Talks samples from `_honors/`**

These starter files belong to neither the Honors collection nor the user's record and must not ship.

**Step 3: Run the focused check**

Run: `python scripts/verify_homepage_content.py`

Expected: Honors assertions pass; the overall command still fails only on the missing style import.

**Step 4: Commit**

```bash
git add _pages/honors.html _honors
git commit -m "feat: add complete honors page"
```

### Task 5: Add restrained responsive presentation styles

**Files:**
- Create: `_sass/layout/_academic-profile.scss`
- Modify: `assets/css/main.scss`

**Step 1: Add scoped styles**

Create styles for `.profile-intro`, `.research-interests`, `.project-grid`, `.project-card`, `.publication-entry`, `.pub-badge`, `.pub-links`, `.honors-timeline`, and `.honor-item`. Use existing theme variables, CSS Grid, visible focus styles, and a single-column mobile breakpoint. Avoid JavaScript and external assets.

**Step 2: Import the partial**

Add `"layout/academic-profile"` after the existing page/archive/sidebar imports in `assets/css/main.scss`.

**Step 3: Run the complete source check**

Run: `python scripts/verify_homepage_content.py`

Expected: PASS with a summary confirming home, publications, honors, and styles.

**Step 4: Commit**

```bash
git add _sass/layout/_academic-profile.scss assets/css/main.scss
git commit -m "style: polish academic profile pages"
```

### Task 6: Correct site metadata and verify the generated site

**Files:**
- Modify: `_config.yml`
- Modify: `_data/navigation.yml`

**Step 1: Correct affected metadata**

Use the canonical GitHub Pages URL without a trailing repository duplication, keep the repository field, remove irrelevant profile placeholders, and ensure Home/Publications/Honors navigation resolves under the configured base URL.

**Step 2: Install existing dependencies if needed**

Run: `bundle install`

Expected: Existing Gemfile dependencies install successfully without changing application architecture.

**Step 3: Build the site**

Run: `bundle exec jekyll build --trace`

Expected: exit code 0 and generated pages under `_site/`, `_site/publications/index.html`, and `_site/honors/index.html`.

**Step 4: Inspect generated output**

Run source and generated-output assertions that confirm all expected section headings, six publications, honors, valid internal URLs, and absence of `Paper Title Number 2`, `Talk 1 on Relevant Topic`, `To be added`, and `GitHub Journal of Bugs`.

Expected: PASS.

**Step 5: Review responsive rendering**

Serve the site locally and inspect Home, Publications, and Honors at desktop and mobile widths. Confirm readable typography, one-column mobile cards, no overlap, and no broken navigation.

**Step 6: Commit**

```bash
git add _config.yml _data/navigation.yml
git commit -m "fix: align site metadata and navigation"
```

### Task 7: Final verification and delivery

**Files:**
- No expected content changes.

**Step 1: Review the diff**

Run: `git diff master...HEAD --check && git diff --stat master...HEAD`

Expected: no whitespace errors; only approved content, style, verification, and plan files changed.

**Step 2: Run all verification again**

Run: `python scripts/verify_homepage_content.py && bundle exec jekyll build --trace`

Expected: both commands pass.

**Step 3: Check worktree state**

Run: `git status --short --branch`

Expected: clean `codex/homepage-refresh` branch.

**Step 4: Prepare publishing handoff**

If authenticated GitHub push access is available, push the branch and open a pull request. Otherwise, provide the local branch and exact push command without exposing or requesting a password or token in chat.
