# Project Template Guide

This guide explains how to add and update content for your research and course projects.

## 📁 File Structure

```
_includes/
  ├── project-styles.html          # Shared CSS styles for all project pages
  ├── project-template.html         # Template for creating new projects
  └── projects/
      ├── cummins.html              # Cummins project content
      ├── infernet.html             # InferNet project content
      ├── irs.html                  # IRS project content
      ├── microprocessor.html       # Microprocessor project content
      ├── pnp-nystra.html           # PnP-Nyström project content
      └── course-project-template.html  # Template for course projects

_pages/
  ├── industry-research.html       # Industry research page (uses includes)
  ├── academic-research.html       # Academic research page (uses includes)
  └── course-projects.html         # Course projects page

images/                             # Place all images here
files/                              # Place PDFs and documents here
```

## 🎨 How to Add/Update Project Content

### For Existing Projects (Industry & Academic Research)

1. **Edit the project include file** in `_includes/projects/`:
   - `cummins.html` - Cummins project
   - `infernet.html` - InferNet project
   - `irs.html` - IRS project
   - `microprocessor.html` - Microprocessor project
   - `pnp-nystra.html` - PnP-Nyström project

2. **Update content sections**:
   - Find the section you want to update (Overview, Methodology, Results, etc.)
   - Replace placeholder text with your actual content
   - Look for `<!-- UPDATE: -->` comments for guidance

3. **Add images/diagrams**:
   ```html
   <!-- Step 1: Save your image to /images/ directory -->
   <!-- Step 2: Uncomment and update the image section: -->
   
   <div class="diagram-container">
     <img src="/images/your-image-name.png" alt="Description of image">
     <p class="diagram-caption">Figure 1: Caption describing the image</p>
   </div>
   ```

### For Course Projects

1. **Copy the template**:
   ```bash
   cp _includes/projects/course-project-template.html _includes/projects/course-project-1.html
   ```

2. **Edit the new file** with your project details

3. **Update course-projects.html**:
   - Add a new tab input:
     ```html
     <input type="radio" id="tab-course-project-1" name="project-tabs" class="project-tab-input" checked>
     ```
   - Add a tab label:
     ```html
     <label for="tab-course-project-1" class="project-tab-label">Your Project Name</label>
     ```
   - Include your project file:
     ```html
     {% raw %}{% include projects/course-project-1.html %}{% endraw %}
     ```

## 📸 Adding Images

### Supported Formats
- PNG (.png) - Best for diagrams, screenshots
- JPEG (.jpg, .jpeg) - Best for photos
- SVG (.svg) - Best for vector graphics
- GIF (.gif) - For animations

### Steps to Add Images

1. **Save your image** to the `/images/` directory
   - Example: `/images/cummins-diagram1.png`

2. **In your project HTML file**, add:
   ```html
   <div class="diagram-container">
     <img src="/images/your-image-name.png" alt="Brief description">
     <p class="diagram-caption">Figure 1: Detailed caption explaining the image</p>
   </div>
   ```

3. **Image sizing**:
   - Recommended width: 800-1200px for diagrams
   - Images will automatically resize to fit the page
   - Use high-quality images for best results

### Extracting Images from PDFs

**On Mac:**
```bash
# Using Preview:
# 1. Open PDF in Preview
# 2. Select the page/image
# 3. File > Export
# 4. Choose PNG or JPEG format
# 5. Save to /images/ directory
```

**Using command line (if ImageMagick installed):**
```bash
convert -density 300 your-file.pdf -quality 100 images/output-%02d.png
```

## 📄 Adding PDFs/Documents

1. **Save PDF** to `/files/` directory
   - Example: `/files/my-report.pdf`

2. **Add link** in project file:
   ```html
   <div class="project-links">
     <a href="/files/my-report.pdf" target="_blank">View Report (PDF)</a>
   </div>
   ```

## 🎯 Content Sections Explained

Each project template includes these sections:

- **Overview**: High-level summary (2-3 sentences)
- **Project Objectives**: List of goals (bullet points)
- **Methodology**: Approach and methods used
- **Key Findings/Contributions**: Important results
- **Technical Approach**: Implementation details
- **Results & Impact**: Outcomes and significance
- **Technologies & Tools**: Tech stack used

### Optional Sections (uncomment to use):

- **Challenges & Solutions**: Problems faced and solutions
- **Future Work**: Potential extensions
- **Visualizations & Diagrams**: Image galleries

## 💡 Tips

1. **Keep content concise**: Each section should be 2-4 bullet points or 1-2 paragraphs
2. **Use images strategically**: Add diagrams for complex concepts
3. **Update regularly**: Keep project pages current with your latest work
4. **Test locally**: Run `jekyll serve` to preview changes before pushing

## 🔧 Troubleshooting

**Images not showing?**
- Check the path: Should start with `/images/` (not `images/`)
- Verify file exists in `/images/` directory
- Check file name matches exactly (case-sensitive)

**Tabs not working?**
- Ensure tab `id` matches the `for` attribute in label
- Check that CSS tab selector includes your tab ID

**Styling issues?**
- All styles are in `_includes/project-styles.html`
- Check browser console for CSS errors

## 📝 Example: Adding a New Course Project

1. Create project file:
   ```bash
   cp _includes/projects/course-project-template.html _includes/projects/ml-course-project.html
   ```

2. Edit `ml-course-project.html` with your content

3. Update `_pages/course-projects.html`:
   ```html
   <input type="radio" id="tab-ml-project" name="project-tabs" class="project-tab-input">
   
   <div class="project-tabs">
     <!-- Add to existing tabs -->
     <label for="tab-ml-project" class="project-tab-label">ML Course Project</label>
   </div>
   
   <div class="project-content-wrapper">
     <!-- Add with other includes -->
     {% raw %}{% include projects/ml-course-project.html %}{% endraw %}
   </div>
   ```

4. Update CSS selector in `course-projects.html`:
   ```css
   #tab-ml-project:checked ~ .project-content-wrapper #ml-project {
     display: block;
   }
   ```

5. Update the `id` in your project HTML to match:
   ```html
   <div id="ml-project" class="project-content">
   ```

That's it! Your new project should appear in the tabs.

