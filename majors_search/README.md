# UNL majors tracker

Search any University of Nebraska–Lincoln major and see its enrollment trend for Fall 2016 through Fall 2025. You can compare up to three majors and filter by level and college.

- `index.html`: the app. It's one static page that uses Chart.js 4.4.1 from jsDelivr.
- `majors.json`: data built from `DR12573 - Majors by College (Fall25-Fall16).xlsx`.
- `build_data.py`: rebuilds `majors.json`. Run `python3 build_data.py "../DR12573 - Majors by College (Fall25-Fall16).xlsx"` (needs `openpyxl`).

You can link directly to a view with the URL hash, for example `#major=JOURNALISM|BROADCASTING&level=0&college=Business`.

## Embedding in a CMS

The page posts its own height to the parent page, so the iframe can grow to fit it with no inner scrollbar. Paste this if your CMS allows scripts in embeds:

```html
<iframe id="unl-majors" src="https://mackenziejevans.github.io/majors_search/"
        title="UNL majors tracker" style="width:100%;border:0;height:900px" loading="lazy"></iframe>
<script>
  (function () {
    var f = document.getElementById("unl-majors");
    window.addEventListener("message", function (e) {
      if (e.source !== f.contentWindow || !e.data) return;
      if (e.data.type === "unl-majors-height") f.style.height = e.data.height + "px";
      if (e.data.type === "unl-majors-scrolltop") f.scrollIntoView({ block: "start", behavior: "smooth" });
    });
  })();
</script>
```

If the CMS strips `<script>`, use the `<iframe>` alone. It stays at a fixed 900px with its own scrollbar, and the filter bar stays pinned to the top of that frame.
