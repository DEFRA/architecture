import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs'
import elkLayouts from 'https://cdn.jsdelivr.net/npm/@mermaid-js/layout-elk@0.1.7/dist/mermaid-layout-elk.esm.min.mjs'

mermaid.registerLayoutLoaders(elkLayouts)
window.mermaid = mermaid
