# Animated websites with zero libraries

*Subtitle: Scroll-driven animation, WebGL backgrounds and page transitions, all with what the browser already ships.*

When we started our Motion series, the obvious move was GSAP. It's excellent, and most animated templates use it. We didn't, for two reasons.

First, licensing. We sell templates that buyers then use for their clients. Whether bundling a third-party animation library into a resold template fits its licence wasn't something we could answer with certainty. "Probably fine" isn't good enough when your buyers build sites for other people.

Second, the browser has caught up. Most of what used to need a library is now built in.

## What we used instead

**CSS scroll-driven animations.** `animation-timeline: view()` ties an animation to an element's position in the viewport. Fade-ins, reveals and parallax without a single scroll listener:

```css
.reveal {
  animation: rise linear both;
  animation-timeline: view();
  animation-range: entry 10% cover 30%;
}
```

**The Web Animations API** for anything triggered by a click or timer: the wedding template's envelope opening, flip-card countdowns, menu transitions. It's the same engine as CSS animations, controlled from JavaScript.

**Canvas and plain WebGL** for the two heavier effects: an ember-particle field on the restaurant template and a shader background on the SaaS template. A small hand-written shader is a few dozen lines and has no dependencies to update.

## Rules we held ourselves to

- **Reduced motion is respected everywhere.** If a visitor has "reduce motion" turned on, every animation switches off and the content is simply there.
- **Nothing is hidden behind animation.** With JavaScript disabled, every section is visible and every button works.
- **Phones first.** Every effect was tested at 390px wide. If it stuttered, it was simplified or dropped.
- **No layout shift.** Animations use transform and opacity only.

## What it costs and what it saves

No library means no version updates, no licence questions, and smaller files. The trade-off is browser support: scroll-driven animations are newer, so on browsers without them, elements simply appear without the effect. For a business website that's the right failure mode. Nobody loses content; some people see less motion.

## See it running

- [Wedding (envelope intro)](https://a0955072107-bit.github.io/-/templates/motion/wedding/en/)
- [Fine dining (ember particles)](https://a0955072107-bit.github.io/-/templates/motion/restaurant/en/)
- [SaaS launch page (WebGL hero)](https://a0955072107-bit.github.io/-/templates/motion/saas/en/)

The five Motion templates are here, each with a licence for client work: [Motion Edition](https://polyglotpages.gumroad.com/l/motion-bundle).
