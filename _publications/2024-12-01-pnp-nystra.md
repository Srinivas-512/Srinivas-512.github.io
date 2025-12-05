---
title: "Plug-and-Play Linear Attention for Pre-trained Image and Video Restoration Models"
collection: publications
category: preprints
permalink: /publication/2025-06-10-pnp-nystra
excerpt: 'We introduce PnP-Nystra, a Nyström-based linear approximation of self-attention, designed as a plug-and-play module for integration into pre-trained image and video restoration models without retraining.'
date: 2025-06-10
venue: 'arXiv preprint'
paperurl: '/files/pnp-nystra.pdf'
citation: 'Kidambi, S., & Nair, P. (2025). Plug-and-Play Linear Attention for Pre-trained Image and Video Restoration Models. <i>arXiv preprint arXiv:2506.08520</i>.'
---

We introduce PnP-Nystra, a Nyström-based linear approximation of self-attention, designed as a plug-and-play module for integration into pre-trained image and video restoration models without retraining. PnP-Nystra serves as a drop-in replacement for multi-head self-attention (MHSA), enabling efficient acceleration in various window-based transformer architectures, including SwinIR, Uformer, and RVRT. Experiments across diverse image and video restoration tasks, such as denoising, deblurring, and super-resolution, demonstrate that PnP-Nystra achieves a 2-4x speed-up on an NVIDIA RTX 4090 GPU and a 2-5x speed-up on CPU inference, with a maximum PSNR drop of only 1.5 dB across all evaluated tasks.

