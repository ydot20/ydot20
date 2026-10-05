#!/usr/bin/env python3
"""Offline checks for the profile's portable, private-by-design SVG artwork."""
from pathlib import Path
import re
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
NS = '{http://www.w3.org/2000/svg}'

class ProfileChecks(unittest.TestCase):
    def test_svg_is_self_contained_and_accessible(self):
        for path in (ROOT/'assets').glob('*.svg'):
            with self.subTest(asset=path.name):
                raw = path.read_text()
                svg = ET.fromstring(raw)
                self.assertEqual(svg.tag, NS+'svg')
                self.assertIsNotNone(svg.find(NS+'title'))
                self.assertIsNotNone(svg.find(NS+'desc'))
                self.assertEqual(svg.attrib['role'], 'img')
                self.assertLess(path.stat().st_size, 100_000)
                for elem in svg.iter():
                    self.assertNotIn(elem.tag, [NS+'script', NS+'foreignObject', NS+'image'])
                    for key, value in elem.attrib.items():
                        self.assertFalse(key.startswith('on'))
                        if key.endswith('href'):
                            self.assertTrue(value.startswith('#'))
                self.assertNotRegex(raw, r'url\(["\x27]?https?:')

    def test_readme_links_and_alt_text(self):
        readme = (ROOT/'README.md').read_text()
        imgs = re.findall(r'<img\b([^>]+)>', readme)
        self.assertEqual(len(imgs), 3)
        for attrs in imgs:
            src = re.search(r'src="([^"]+)"', attrs).group(1)
            self.assertTrue((ROOT/src).is_file())
            self.assertRegex(attrs, r'alt="[^"]{30,}"')
            self.assertIn('width="100%"', attrs)
        self.assertIn('AI assistant powered by OpenAI', readme)
        self.assertIn('not a contribution graph', readme)
        self.assertIn('уdot_2.0', readme)

    def test_reduced_motion_and_no_workflows(self):
        for name in ['workshop.svg', 'duck-route.svg']:
            raw=(ROOT/'assets'/name).read_text()
            self.assertIn('@media(prefers-reduced-motion:reduce)', raw)
            self.assertIn('animation:none!important', raw)
        self.assertFalse((ROOT/'.github/workflows').exists())

if __name__ == '__main__':
    unittest.main()
