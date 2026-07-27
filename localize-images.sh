#!/bin/bash
# The site currently loads photos directly from the old Wix CDN (so everything works
# with zero setup). Before you cancel the Wix subscription, run this ONCE from the
# repo root to copy every image into images/ (with SEO filenames) and rewrite all
# HTML/CSS references to the site's own copies. Then commit and push.
#   bash localize-images.sh
set -e
mkdir -p images
curl -fL "https://static.wixstatic.com/media/700ba3_c949a1b7dee846a5abdd7d84495fe296~mv2.png" -o "images/junk-removal-big-bear-lake-hero.png"
curl -fL "https://static.wixstatic.com/media/700ba3_6565886a9361472b83c96bd5b11d4399~mv2.jpeg" -o "images/cabin-junk-removal-big-bear.jpg"
curl -fL "https://static.wixstatic.com/media/700ba3_c76abc7200244b52a227c1e9dcb918f3~mv2.jpg" -o "images/pine-needle-removal-fire-abatement-big-bear.jpg"
curl -fL "https://static.wixstatic.com/media/700ba3_4656c39235b54ef9b939c2b495db6b3b~mv2.jpeg" -o "images/airbnb-turnover-cleanout-big-bear-lake.jpg"
curl -fL "https://static.wixstatic.com/media/700ba3_145bead2c2f04eb0a6cdf823ab023245~mv2.jpg" -o "images/appliance-removal-big-bear-ca.jpg"
curl -fL "https://static.wixstatic.com/media/700ba3_2a5f170845884bf393777f0238f2f2b9~mv2.jpeg" -o "images/shed-demolition-removal-big-bear.jpg"
curl -fL "https://static.wixstatic.com/media/700ba3_b5b53d3d8d5e4a5d8958ff5cd43f3a63~mv2.jpg" -o "images/local-moving-hauling-big-bear.jpg"
curl -fL "https://static.wixstatic.com/media/700ba3_de2391c1d636438dbc7bf4acc38f34a0~mv2.jpg" -o "images/weed-abatement-fire-risk-big-bear.jpg"
curl -fL "https://static.wixstatic.com/media/700ba3_6616411fd5e64924bc35ae30073d30f2~mv2.jpg" -o "images/tree-shrub-trimming-ladder-fuel-big-bear.jpg"
curl -fL "https://static.wixstatic.com/media/700ba3_edf2488d9cb940a69bf82108debe2a59~mv2.jpg" -o "images/defensible-space-clearing-big-bear-cabin.jpg"
curl -fL "https://static.wixstatic.com/media/700ba3_a60e2df95a1c4730a8d0e03566a498c7~mv2.jpeg" -o "images/weed-abatement-crew-big-bear.jpg"
curl -fL "https://static.wixstatic.com/media/700ba3_291abe19d26a45ab99786cafcb8855c9~mv2.jpg" -o "images/hot-tub-removal-big-bear-airbnb.jpg"
curl -fL "https://static.wixstatic.com/media/700ba3_400fe33d87254ed485e45d2add33c608~mv2.jpeg" -o "images/furniture-swap-hauling-big-bear-str.jpg"
curl -fL "https://static.wixstatic.com/media/700ba3_84d217f13c404bb59dd1ffbeddbf78c6~mv2.png" -o "images/junk-removal-service-area-map-big-bear-valley.png"
curl -fL "https://static.wixstatic.com/media/700ba3_fcf0e1c21f9243f1a5ec97f2f85171be~mv2.png" -o "images/junk-removal-big-bear-logo.png"
echo "✅ Images downloaded into images/ — rewriting references..."
grep -rl 'https://static.wixstatic.com/media/700ba3_c949a1b7dee846a5abdd7d84495fe296~mv2.png' --include='*.html' --include='*.css' . | xargs -r sed -i.bak 's|https://static.wixstatic.com/media/700ba3_c949a1b7dee846a5abdd7d84495fe296~mv2.png|/images/junk-removal-big-bear-lake-hero.png|g'
grep -rl 'https://static.wixstatic.com/media/700ba3_6565886a9361472b83c96bd5b11d4399~mv2.jpeg' --include='*.html' --include='*.css' . | xargs -r sed -i.bak 's|https://static.wixstatic.com/media/700ba3_6565886a9361472b83c96bd5b11d4399~mv2.jpeg|/images/cabin-junk-removal-big-bear.jpg|g'
grep -rl 'https://static.wixstatic.com/media/700ba3_c76abc7200244b52a227c1e9dcb918f3~mv2.jpg' --include='*.html' --include='*.css' . | xargs -r sed -i.bak 's|https://static.wixstatic.com/media/700ba3_c76abc7200244b52a227c1e9dcb918f3~mv2.jpg|/images/pine-needle-removal-fire-abatement-big-bear.jpg|g'
grep -rl 'https://static.wixstatic.com/media/700ba3_4656c39235b54ef9b939c2b495db6b3b~mv2.jpeg' --include='*.html' --include='*.css' . | xargs -r sed -i.bak 's|https://static.wixstatic.com/media/700ba3_4656c39235b54ef9b939c2b495db6b3b~mv2.jpeg|/images/airbnb-turnover-cleanout-big-bear-lake.jpg|g'
grep -rl 'https://static.wixstatic.com/media/700ba3_145bead2c2f04eb0a6cdf823ab023245~mv2.jpg' --include='*.html' --include='*.css' . | xargs -r sed -i.bak 's|https://static.wixstatic.com/media/700ba3_145bead2c2f04eb0a6cdf823ab023245~mv2.jpg|/images/appliance-removal-big-bear-ca.jpg|g'
grep -rl 'https://static.wixstatic.com/media/700ba3_2a5f170845884bf393777f0238f2f2b9~mv2.jpeg' --include='*.html' --include='*.css' . | xargs -r sed -i.bak 's|https://static.wixstatic.com/media/700ba3_2a5f170845884bf393777f0238f2f2b9~mv2.jpeg|/images/shed-demolition-removal-big-bear.jpg|g'
grep -rl 'https://static.wixstatic.com/media/700ba3_b5b53d3d8d5e4a5d8958ff5cd43f3a63~mv2.jpg' --include='*.html' --include='*.css' . | xargs -r sed -i.bak 's|https://static.wixstatic.com/media/700ba3_b5b53d3d8d5e4a5d8958ff5cd43f3a63~mv2.jpg|/images/local-moving-hauling-big-bear.jpg|g'
grep -rl 'https://static.wixstatic.com/media/700ba3_de2391c1d636438dbc7bf4acc38f34a0~mv2.jpg' --include='*.html' --include='*.css' . | xargs -r sed -i.bak 's|https://static.wixstatic.com/media/700ba3_de2391c1d636438dbc7bf4acc38f34a0~mv2.jpg|/images/weed-abatement-fire-risk-big-bear.jpg|g'
grep -rl 'https://static.wixstatic.com/media/700ba3_6616411fd5e64924bc35ae30073d30f2~mv2.jpg' --include='*.html' --include='*.css' . | xargs -r sed -i.bak 's|https://static.wixstatic.com/media/700ba3_6616411fd5e64924bc35ae30073d30f2~mv2.jpg|/images/tree-shrub-trimming-ladder-fuel-big-bear.jpg|g'
grep -rl 'https://static.wixstatic.com/media/700ba3_edf2488d9cb940a69bf82108debe2a59~mv2.jpg' --include='*.html' --include='*.css' . | xargs -r sed -i.bak 's|https://static.wixstatic.com/media/700ba3_edf2488d9cb940a69bf82108debe2a59~mv2.jpg|/images/defensible-space-clearing-big-bear-cabin.jpg|g'
grep -rl 'https://static.wixstatic.com/media/700ba3_a60e2df95a1c4730a8d0e03566a498c7~mv2.jpeg' --include='*.html' --include='*.css' . | xargs -r sed -i.bak 's|https://static.wixstatic.com/media/700ba3_a60e2df95a1c4730a8d0e03566a498c7~mv2.jpeg|/images/weed-abatement-crew-big-bear.jpg|g'
grep -rl 'https://static.wixstatic.com/media/700ba3_291abe19d26a45ab99786cafcb8855c9~mv2.jpg' --include='*.html' --include='*.css' . | xargs -r sed -i.bak 's|https://static.wixstatic.com/media/700ba3_291abe19d26a45ab99786cafcb8855c9~mv2.jpg|/images/hot-tub-removal-big-bear-airbnb.jpg|g'
grep -rl 'https://static.wixstatic.com/media/700ba3_400fe33d87254ed485e45d2add33c608~mv2.jpeg' --include='*.html' --include='*.css' . | xargs -r sed -i.bak 's|https://static.wixstatic.com/media/700ba3_400fe33d87254ed485e45d2add33c608~mv2.jpeg|/images/furniture-swap-hauling-big-bear-str.jpg|g'
grep -rl 'https://static.wixstatic.com/media/700ba3_84d217f13c404bb59dd1ffbeddbf78c6~mv2.png' --include='*.html' --include='*.css' . | xargs -r sed -i.bak 's|https://static.wixstatic.com/media/700ba3_84d217f13c404bb59dd1ffbeddbf78c6~mv2.png|/images/junk-removal-service-area-map-big-bear-valley.png|g'
grep -rl 'https://static.wixstatic.com/media/700ba3_fcf0e1c21f9243f1a5ec97f2f85171be~mv2.png' --include='*.html' --include='*.css' . | xargs -r sed -i.bak 's|https://static.wixstatic.com/media/700ba3_fcf0e1c21f9243f1a5ec97f2f85171be~mv2.png|/images/junk-removal-big-bear-logo.png|g'
find . -name '*.bak' -delete
echo "✅ Done. Review with git diff, then commit and push."
