const _0x72de = ['html', 'country', 'flag', 'critical', 'casesPerOneMillion', '\x22\x20class=\x22img-fluid\x20mr-3\x22\x20width=\x2270\x22\x20/>', 'each', '#country_recovered', '<br/>\x20Cases:\x20', '#country_todayDeaths', '#continent-map', 'cases', '<br/>\x20Death:\x20', '\x22\x20width=\x2225\x22\x20class=\x22mr-2\x20mb-1\x20\x22\x20/>', '#country_casesPerOneMillion', 'countryInfo', 'deaths', 'todayCases', 'toLowerCase', '#7B6FFF', '<img\x20src=\x22', '#country_critical', 'log', 'json', 'ajax', '#country_deaths', 'https://corona.lmao.ninja/v2/countries', 'iso2', 'todayDeaths', 'deathsPerOneMillion', '#country_todayCases', '#country_name', 'active', 'europe_en', '#f00000', 'polynomial', 'entries', 'toUpperCase', 'recovered'];
(function (_0x428699, _0x72def8) {
	const _0x43a9b5 = function (_0x359040) {
		while (--_0x359040) {
			_0x428699['push'](_0x428699['shift']());
		}
	};
	_0x43a9b5(++_0x72def8);
}(_0x72de, 0x17b));
const _0x43a9 = function (_0x428699, _0x72def8) {
	_0x428699 = _0x428699 - 0x0;
	let _0x43a9b5 = _0x72de[_0x428699];
	return _0x43a9b5;
};
$(function () {
	const _0x45f3a = $(_0x43a9('0x3'));
	const _0x5e2508 = $('#country_flag');
	const _0x571525 = $('#country_cases');
	const _0x51bada = $('#country_active');
	const _0x453547 = $(_0x43a9('0x20'));
	const _0x4c3131 = $(_0x43a9('0x24'));
	const _0x4fd7fa = $(_0x43a9('0x12'));
	const _0x51a551 = $(_0x43a9('0x2'));
	const _0x35a6c5 = $(_0x43a9('0x14'));
	const _0x1d3d8d = $(_0x43a9('0x19'));
	const _0x34857b = $('#country_deathsPerOneMillion');
	$[_0x43a9('0x23')]({
		'type': 'GET',
		'url': _0x43a9('0x25'),
		'dataType': _0x43a9('0x22'),
		'success': function (_0x59f25b) {
			$[_0x43a9('0x11')](_0x59f25b, function (_0x22d82c, _0x54c400) {
				vgg = _0x54c400[_0x43a9('0x1a')]['iso2'];
				if (vgg == 'ES') {
					_0x45f3a[_0x43a9('0xb')](_0x54c400[_0x43a9('0xc')]);
					_0x5e2508[_0x43a9('0xb')](_0x43a9('0x1f') + _0x54c400[_0x43a9('0x1a')]['flag'] + _0x43a9('0x10'));
					_0x571525[_0x43a9('0xb')](_0x54c400[_0x43a9('0x16')]);
					_0x51bada['html'](_0x54c400[_0x43a9('0x4')]);
					_0x453547['html'](_0x54c400[_0x43a9('0xe')]);
					_0x4c3131[_0x43a9('0xb')](_0x54c400['deaths']);
					_0x4fd7fa[_0x43a9('0xb')](_0x54c400[_0x43a9('0xa')]);
					_0x51a551[_0x43a9('0xb')](_0x54c400[_0x43a9('0x1c')]);
					_0x35a6c5[_0x43a9('0xb')](_0x54c400[_0x43a9('0x0')]);
					_0x1d3d8d[_0x43a9('0xb')](_0x54c400[_0x43a9('0xf')]);
					_0x34857b[_0x43a9('0xb')](_0x54c400[_0x43a9('0x1')]);
				}
			});
			sample_data = {};
			$[_0x43a9('0x11')](_0x59f25b, function (_0xc1cb7, _0x8779dc) {
				var _0x1e7a6b = _0x8779dc['countryInfo'][_0x43a9('0x26')];
				var _0x5a4e29 = _0x8779dc[_0x43a9('0x16')];
				sample_data[_0x1e7a6b] = _0x5a4e29;
			});
			const _0x31fe89 = {};
			for (const [_0x2df0d0, _0xfaafe1] of Object[_0x43a9('0x8')](sample_data)) {
				_0x31fe89[_0x2df0d0[_0x43a9('0x1d')]()] = _0xfaafe1;
			}
			$(_0x43a9('0x15'))['vectorMap']({
				'map': _0x43a9('0x5'),
				'backgroundColor': null,
				'selectedRegions': 'es',
				'color': '#ddd',
				'hoverOpacity': 0.7,
				'selectedColor': _0x43a9('0x1e'),
				'values': _0x31fe89,
				'scaleColors': [_0x43a9('0x6'), '#000000'],
				'normalizeFunction': _0x43a9('0x7'),
				'onRegionClick': function (_0x5d1813, _0x51415a, _0x529963) {
					console[_0x43a9('0x21')](_0x51415a);
					vfv = _0x51415a[_0x43a9('0x9')]();
					$[_0x43a9('0x11')](_0x59f25b, function (_0x2aa5d2, _0x59baf0) {
						vgg = _0x59baf0['countryInfo']['iso2'];
						if (vfv == vgg) {
							_0x45f3a[_0x43a9('0xb')](_0x59baf0[_0x43a9('0xc')]);
							_0x5e2508['html'](_0x43a9('0x1f') + _0x59baf0[_0x43a9('0x1a')][_0x43a9('0xd')] + _0x43a9('0x10'));
							_0x571525[_0x43a9('0xb')](_0x59baf0['cases']);
							_0x51bada[_0x43a9('0xb')](_0x59baf0['active']);
							_0x453547[_0x43a9('0xb')](_0x59baf0['critical']);
							_0x4c3131['html'](_0x59baf0[_0x43a9('0x1b')]);
							_0x4fd7fa[_0x43a9('0xb')](_0x59baf0['recovered']);
							_0x51a551[_0x43a9('0xb')](_0x59baf0[_0x43a9('0x1c')]);
							_0x35a6c5[_0x43a9('0xb')](_0x59baf0[_0x43a9('0x0')]);
							_0x1d3d8d[_0x43a9('0xb')](_0x59baf0[_0x43a9('0xf')]);
							_0x34857b[_0x43a9('0xb')](_0x59baf0[_0x43a9('0x1')]);
						}
					});
				},
				'onLabelShow': function (_0x2941a8, _0x26de26, _0x6e2c1) {
					vfv = _0x6e2c1[_0x43a9('0x9')]();
					$[_0x43a9('0x11')](_0x59f25b, function (_0x5619ed, _0x1b7534) {
						vgg = _0x1b7534[_0x43a9('0x1a')][_0x43a9('0x26')];
						if (vfv == vgg) {
							_0x26de26[_0x43a9('0xb')](_0x43a9('0x1f') + _0x1b7534[_0x43a9('0x1a')][_0x43a9('0xd')] + _0x43a9('0x18') + _0x1b7534[_0x43a9('0xc')] + _0x43a9('0x13') + _0x1b7534[_0x43a9('0x16')] + _0x43a9('0x17') + _0x1b7534[_0x43a9('0x1b')] + '<br/>\x20Active:\x20' + _0x1b7534[_0x43a9('0x4')] + '<br/>\x20Recovered\x20' + _0x1b7534[_0x43a9('0xa')]);
						}
					});
				}
			});
		}
	});
});