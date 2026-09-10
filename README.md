# ReWallet merchant assets

Logo and cover images for merchants in the ReWallet loyalty app, served raw from GitHub so `merchant.logoUrl` / `merchant.coverImageUrl` point at stable, public, non-expiring URLs (Facebook / Instagram CDN links expire and return 403).

## Layout

One folder per merchant, kebab-case:

```
<merchant-slug>/
  <merchant_slug>_logo.png    square-ish mark, rendered in a 50px circle
  <merchant_slug>_cover.jpg   wide photo, rendered as the card detail header
```

## URLs

```
https://raw.githubusercontent.com/ahiad93/rewallet-merchant-assets/main/<merchant-slug>/<file>
```

## Merchants

| Merchant | Logo | Cover |
|---|---|---|
| Juice & more | `juice-and-more/juice_and_more_logo.png` | `juice-and-more/juice_and_more_cover.jpg` |
| מדאמס (Maddamas) | `maddamas/maddamas_logo.png` | `maddamas/maddamas_cover.jpg` |
