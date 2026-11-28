Source for generated files. Not part of the site.

- gen.py builds every page of the site (index, about, schedule, host, attend, thanks).
- guides/docs.py builds the Host Guide and Sponsor Guide PDFs in assets/docs/.
  Render: serve the repo root on :8765, run docs.py (it writes _docs/*.html plus docs.css), then print each page to Letter PDF with Chrome (portrait for host, landscape for sponsor).
