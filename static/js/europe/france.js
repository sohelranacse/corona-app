var _0x14d7 = ['nearest', 'formatToParts', '#6456FF', 'height', 'https://pomber.github.io/covid19/timeseries.json', 'short', 'Value', 'length', 'index', '#2DCE99', 'Death', 'France', 'json', 'map', 'ajax', 'getElementById', 'confirmed', 'max', 'top', 'deaths', '#F7F8FC', 'slice', 'DateTimeFormat', 'Recovered', '#F5385A', '2-digit', 'Month', 'france_timeseries', 'transparent', 'Confirmed'];
(function (_0x1ca8bd, _0x14d795) {
	var _0x3ef392 = function (_0x133590) {
		while (--_0x133590) {
			_0x1ca8bd['push'](_0x1ca8bd['shift']());
		}
	};
	_0x3ef392(++_0x14d795);
}(_0x14d7, 0xdc));
var _0x3ef3 = function (_0x1ca8bd, _0x14d795) {
	_0x1ca8bd = _0x1ca8bd - 0x0;
	var _0x3ef392 = _0x14d7[_0x1ca8bd];
	return _0x3ef392;
};
$(function () {
	$[_0x3ef3('0x4')]({
		'type': 'GET',
		'url': _0x3ef3('0x18'),
		'dataType': _0x3ef3('0x2'),
		'success': function (_0x100e34) {
			var _0x5dcfc4 = _0x100e34[_0x3ef3('0x1')][_0x3ef3('0xb')](Math[_0x3ef3('0x7')](_0x100e34['France'][_0x3ef3('0x1b')] - 0x1e, 0x1))[_0x3ef3('0x3')](_0x2790f0 => _0x2790f0[_0x3ef3('0x6')]);
			var _0x5b44fe = _0x100e34[_0x3ef3('0x1')][_0x3ef3('0xb')](Math[_0x3ef3('0x7')](_0x100e34[_0x3ef3('0x1')][_0x3ef3('0x1b')] - 0x1e, 0x1))[_0x3ef3('0x3')](_0x4d8bc7 => _0x4d8bc7[_0x3ef3('0x9')]);
			var _0x15d8a3 = _0x100e34['France'][_0x3ef3('0xb')](Math['max'](_0x100e34[_0x3ef3('0x1')]['length'] - 0x1e, 0x1))[_0x3ef3('0x3')](_0x25baa2 => _0x25baa2['recovered']);
			var _0x1d1af6 = _0x100e34[_0x3ef3('0x1')][_0x3ef3('0xb')](Math['max'](_0x100e34['France'][_0x3ef3('0x1b')] - 0x1e, 0x1))[_0x3ef3('0x3')](function (_0x4ea1a1) {
				const _0x4d5e80 = new Date(_0x4ea1a1['date']);
				const _0x1c3ad8 = new Intl[(_0x3ef3('0xc'))]('en', {
					'year': 'numeric',
					'month': _0x3ef3('0x19'),
					'day': _0x3ef3('0xf')
				});
				const [{
					value: _0x3ba1f9
				}, , {
					value: _0x1fc812
				}] = _0x1c3ad8[_0x3ef3('0x15')](_0x4d5e80);
				return _0x1fc812 + '-' + _0x3ba1f9;
			});
			var _0x54d1c4 = document[_0x3ef3('0x5')](_0x3ef3('0x11'));
			_0x54d1c4[_0x3ef3('0x17')] = 0x64;
			new Chart(_0x54d1c4, {
				'type': 'line',
				'data': {
					'labels': _0x1d1af6,
					'datasets': [{
						'label': _0x3ef3('0x13'),
						'borderColor': _0x3ef3('0x16'),
						'borderWidth': '2',
						'backgroundColor': 'transparent',
						'pointBackgroundColor': _0x3ef3('0x16'),
						'data': _0x5dcfc4
					}, {
						'label': _0x3ef3('0x0'),
						'borderColor': _0x3ef3('0xe'),
						'borderWidth': '2',
						'backgroundColor': _0x3ef3('0x12'),
						'pointBackgroundColor': '#F5385A',
						'data': _0x5b44fe
					}, {
						'label': _0x3ef3('0xd'),
						'borderColor': '#2DCE99',
						'borderWidth': '2',
						'backgroundColor': _0x3ef3('0x12'),
						'pointBackgroundColor': _0x3ef3('0x1d'),
						'data': _0x15d8a3
					}]
				},
				'options': {
					'responsive': !![],
					'maintainAspectRatio': ![],
					'legend': {
						'display': !![],
						'position': _0x3ef3('0x8'),
						'labels': {
							'usePointStyle': !![]
						}
					},
					'tooltips': {
						'mode': _0x3ef3('0x1c'),
						'intersect': ![]
					},
					'hover': {
						'mode': _0x3ef3('0x14'),
						'intersect': !![]
					},
					'scales': {
						'xAxes': [{
							'display': !![],
							'gridLines': {
								'display': !![],
								'drawBorder': ![],
								'color': '#F7F8FC'
							},
							'scaleLabel': {
								'display': ![],
								'labelString': _0x3ef3('0x10')
							}
						}],
						'yAxes': [{
							'display': !![],
							'gridLines': {
								'display': !![],
								'drawBorder': ![],
								'color': _0x3ef3('0xa')
							},
							'scaleLabel': {
								'display': !![],
								'labelString': _0x3ef3('0x1a')
							}
						}]
					}
				}
			});
		}
	});
});