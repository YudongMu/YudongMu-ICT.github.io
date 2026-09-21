# Academic Homepage Content Refresh Design

## Goal

Turn the current Academic Pages starter site into a complete, credible academic homepage that reflects Yudong Mu's research, publications, and honors. The site remains English-first, while the Chinese title and venue of the *Journal of Computer Research and Development* paper remain in Chinese to match the official publication.

## Scope

- Preserve the current Jekyll/Academic Pages architecture, navigation pattern, and author sidebar.
- Refresh the home page with a concise biography, research interests, education, selected projects, and industry experience.
- Complete the Publications page with all six publications from the latest two-page CV.
- Replace the broken Honors/Talks placeholder with a real Honors page.
- Apply a small, maintainable presentation layer for project cards, publication metadata, badges, and an honors timeline.
- Correct broken URLs, placeholder metadata, spelling mistakes, and template content encountered in the affected pages.

## Content Strategy

The home page presents a broad research identity: AI inference acceleration, dataflow architectures, CGRA mapping, and hardware/software co-design. It does not feature the dLLM reproduction work as a selected project. The selected projects are:

1. FDHA: diffusion-model heterogeneous acceleration.
2. DFU-Y: dataflow optimization for YOLO workloads.
3. GenCNN: multi-objective mapping for CNN accelerators.
4. NFMap: node-fusion optimization for CGRA mapping.

The Zhongke Ruixin internship appears separately under Industry Experience, emphasizing DPU deployment, simulator/RTL development, mapping, scheduling, and routing.

## Information Architecture

### Home

The home page contains:

- A compact professional introduction.
- Research Interests.
- Education.
- Selected Research Projects, displayed as responsive cards with short outcome-focused summaries and links to associated publications.
- Industry Experience.
- A concise contact line that complements the author sidebar.

### Publications

Publications remain a Jekyll collection and are grouped into Journal Articles and Conference Papers. Each entry contains the complete author list, official title, venue, year, classification where relevant, and a DOI or paper link when available. Yudong Mu's name is emphasized. The Chinese journal entry retains its official Chinese title and venue name.

The six entries are GenCNN, the YOLO dataflow paper, FDHA, NFMap, A2RT, and the RISC-V extended CNN infrastructure paper. Template/sample publications are removed from the rendered collection.

### Honors

The `/honors/` page becomes a real archive-style page with dated groups for graduate and undergraduate honors. It includes the UCAS Outstanding Student Model honor, National Scholarship for Graduate Students, E Fund Freshman Scholarship, UCAS Outstanding Student, undergraduate second-class scholarships, Outstanding Student honors, and Outstanding Student Leader honor.

## Presentation

The existing theme remains the visual foundation. A small custom SCSS partial supplies:

- Responsive project cards.
- Compact metadata rows and classification badges.
- A simple honors timeline/list.
- Consistent spacing, color, and hover states aligned with the existing blue-gray palette.

No JavaScript framework or new runtime dependency is introduced.

## Data Flow and Maintenance

Home-page project content lives in `_pages/about.md`. Publication records remain separate Markdown files in `_publications/`, so future papers can be added independently. Honors content lives directly in `_pages/honors.html` because it is short and changes infrequently. Navigation remains in `_data/navigation.yml`.

## Error Handling and Compatibility

- Use only GitHub Pages-compatible Jekyll and Liquid features.
- Avoid external assets for core layout so the page remains usable if third-party services fail.
- Keep links explicit and validate every DOI/paper URL.
- Ensure cards collapse to one column on small screens.
- Preserve existing redirects for the home page.

## Verification

- Run a Jekyll build and treat build failures as blocking.
- Check generated `/`, `/publications/`, and `/honors/` pages for expected headings, content, and links.
- Confirm no sample publication or talk placeholder appears in generated output.
- Check links and HTML structure with automated text assertions.
- Review the three pages at desktop and mobile widths in a local browser when the environment supports it.

## Delivery

Changes are prepared on the `codex/homepage-refresh` branch. Publishing requires authenticated GitHub push access; local implementation and verification do not require credentials.
