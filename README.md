# Sockpuppet Detection System (Proposal)

A modular toolchain for identifying and investigating coordinated inauthentic behavior ("sockpuppets") on Twitter/X, built for law enforcement and OSINT professionals.

---

## 🧭 Project Purpose

This tool detects and analyzes suspected sockpuppet accounts using a hybrid approach that combines:
- API-based tweet and account metadata retrieval (via [SocialData.tools](https://docs.socialdata.tools))
- Headless browser automation for visual and behavioral profiling (via Playwright)
- Stylometric and behavioral clustering for pattern recognition
- Legally defensible logging and data preservation

---

## 🧱 System Architecture

```plaintext
┌──────────────┐
│ Entry Points │  ← Known account, tweet, or hashtag
└──────┬───────┘
       ↓
┌────────────────────┐
│ SocialData API Core│ ← Tweet/account metadata, metrics, timelines
└──────┬─────────────┘
       ↓
┌─────────────────────────────┐
│ Metadata Feature Extractor  │ ← Source app, device, times, bio, lang
└──────┬──────────────────────┘
       ↓
┌────────────────────────────┐
│ Sockpuppet Scoring Engine  │ ← Stylometry + behavior clustering
└──────┬─────────────────────┘
       ↓
┌───────────────────────┐
│ Playwright Augmentation│ ← Visual scrape of UI-only features
└──────┬────────────────┘
       ↓
┌──────────────────────┐
│ Case Builder + Export│ ← Evidence log, screenshots, JSON output
└──────────────────────┘
