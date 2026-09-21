---
permalink: /
title: "About Me"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

<div class="profile-intro" markdown="1">

I am **Yudong Mu (穆宇栋)**, a Ph.D. candidate in Computer Architecture at the [Institute of Computing Technology, Chinese Academy of Sciences](http://www.ict.ac.cn/), where I work in the State Key Laboratory of Processors.

My research explores efficient AI systems across **model analysis, compiler mapping, and accelerator architecture**. I am particularly interested in turning workload characteristics into practical dataflows, scheduling strategies, and hardware/software co-designs.

</div>

## Research Interests

<div class="research-interests" aria-label="Research interests">
  <span>AI Inference Acceleration</span>
  <span>Dataflow Architectures</span>
  <span>CGRA Mapping</span>
  <span>Compiler &amp; Runtime Optimization</span>
  <span>Hardware/Software Co-design</span>
</div>

## Education

<div class="education-list">
  <div class="education-item">
    <div>
      <strong>Institute of Computing Technology, Chinese Academy of Sciences</strong><br>
      Ph.D. candidate in Computer Architecture · State Key Laboratory of Processors
    </div>
    <time>2023–Present</time>
  </div>
  <div class="education-item">
    <div>
      <strong>University of Chinese Academy of Sciences</strong><br>
      B.Eng. in Electronic and Information Engineering
    </div>
    <time>2019–2023</time>
  </div>
</div>

## Selected Research Projects

<div class="project-grid">
  <article class="project-card">
    <div class="project-card__meta">First author · Euro-Par 2025 · CCF-B</div>
    <h3><a href="{{ '/publication/2025-fdha/' | relative_url }}">FDHA: Heterogeneous Acceleration for Diffusion Models</a></h3>
    <p>Developed cross-operator dataflow fusion and a PE/TPE heterogeneous pipeline for the alternating ResNet and Transformer workloads in Stable Diffusion. FDHA achieved average speedups of <strong>3.28×</strong> over NVIDIA A100 and <strong>2.62×</strong> over prior diffusion accelerators.</p>
  </article>

  <article class="project-card">
    <div class="project-card__meta">First author · Journal paper · T1</div>
    <h3><a href="{{ '/publication/2025-yolo-dataflow/' | relative_url }}">DFU-Y: Dataflow Optimization for YOLO</a></h3>
    <p>Designed dataflow-graph mapping, operator-fusion scheduling, and double buffering for small-kernel convolutions in YOLO. The resulting architecture improved performance by <strong>2.527×</strong> and energy efficiency by <strong>2.658×</strong> over a general-purpose dataflow baseline.</p>
  </article>

  <article class="project-card">
    <div class="project-card__meta">First author · ACM TACO 2025 · CCF-A</div>
    <h3><a href="{{ '/publication/2025-gencnn/' | relative_url }}">GenCNN: Multi-objective CNN Accelerator Mapping</a></h3>
    <p>Built an NSGA-II-based framework that jointly optimizes task partitioning, convolution parallelism, scheduling, and routing. Compared with AutoTVM, GenCNN delivered average improvements of <strong>17.66×</strong> in compilation speed and <strong>6.47×</strong> in execution speed.</p>
  </article>

  <article class="project-card">
    <div class="project-card__meta">Co-first author · APPT 2025 · CCF-C</div>
    <h3><a href="{{ '/publication/2025-nfmap/' | relative_url }}">NFMap: Node-fusion Optimization for CGRA Mapping</a></h3>
    <p>Introduced network-flow-constrained node fusion to reduce routing pressure from long dependencies in CGRAs. NFMap improved mapping quality by <strong>1.43×</strong> and compilation speed by <strong>1.14×</strong> on average over E2EMap.</p>
  </article>
</div>

## Industry Experience

<div class="experience-item">
  <div class="experience-item__heading">
    <div><strong>Zhongke Ruixin · Chip Development and Application Software Performance Optimization Intern</strong></div>
    <time>Jul. 2024–Sep. 2025</time>
  </div>
  <ul>
    <li>Deployed and optimized YOLO convolution operators and general neural networks on a dataflow processing unit (DPU), with work spanning graph mapping, scheduling, and routing.</li>
    <li>Developed approximately 4,000 lines of C for a microcontroller simulator supporting dynamic scheduling, together with corresponding RTL-level Verilog functionality.</li>
    <li>Studied diffusion-model deployment on the DPU and co-optimized cross-operator dataflows with the underlying architecture.</li>
  </ul>
</div>

## Contact

For research discussions or collaboration, please email [muyudong19@mails.ucas.ac.cn](mailto:muyudong19@mails.ucas.ac.cn).
