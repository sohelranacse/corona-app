var _0x34b5 = ['numeric', 'Spain', 'map', '#6456FF', '#F7F8FC', 'DateTimeFormat', 'json', 'ajax', 'length', 'Confirmed', 'max', 'spain_timeseries', 'confirmed', 'deaths', 'slice', 'line', 'Value', 'https://pomber.github.io/covid19/timeseries.json', '#2DCE99', 'transparent', 'recovered', 'formatToParts', 'short', '#F5385A', 'date', 'Month', 'height', 'nearest', '2-digit', 'index', 'Recovered'];
(function (_0x4ad181, _0x34b5c1) {
	var _0x246370 = function (_0x249d5b) {
		while (--_0x249d5b) {
			_0x4ad181['push'](_0x4ad181['shift']());
		}
	};
	_0x246370(++_0x34b5c1);
}(_0x34b5, 0x77));
var _0x2463 = function (_0x4ad181, _0x34b5c1) {
	_0x4ad181 = _0x4ad181 - 0x0;
	var _0x246370 = _0x34b5[_0x4ad181];
	return _0x246370;
};
$(function () {
	$[_0x2463('0xc')]({
		'type': 'GET',
		'url': _0x2463('0x16'),
		'dataType': _0x2463('0xb'),
		'success': function (_0x5af130) {
			var _0x5775ae = _0x5af130['Spain'][_0x2463('0x13')](Math[_0x2463('0xf')](_0x5af130[_0x2463('0x6')][_0x2463('0xd')] - 0x1e, 0x1))['map'](_0x2b56e9 => _0x2b56e9[_0x2463('0x11')]);
			var _0x40dde8 = _0x5af130[_0x2463('0x6')][_0x2463('0x13')](Math[_0x2463('0xf')](_0x5af130[_0x2463('0x6')][_0x2463('0xd')] - 0x1e, 0x1))[_0x2463('0x7')](_0x5bbf27 => _0x5bbf27[_0x2463('0x12')]);
			var _0x491129 = _0x5af130[_0x2463('0x6')][_0x2463('0x13')](Math[_0x2463('0xf')](_0x5af130[_0x2463('0x6')]['length'] - 0x1e, 0x1))['map'](_0x1a91c5 => _0x1a91c5[_0x2463('0x19')]);
			var _0x53619a = _0x5af130[_0x2463('0x6')][_0x2463('0x13')](Math[_0x2463('0xf')](_0x5af130[_0x2463('0x6')][_0x2463('0xd')] - 0x1e, 0x1))[_0x2463('0x7')](function (_0x52ab6d) {
				const _0x23c5b8 = new Date(_0x52ab6d[_0x2463('0x1d')]);
				const _0x436acb = new Intl[(_0x2463('0xa'))]('en', {
					'year': _0x2463('0x5'),
					'month': _0x2463('0x1b'),
					'day': _0x2463('0x2')
				});
				const [{
					value: _0x179590
				}, , {
					value: _0x57f079
				}] = _0x436acb[_0x2463('0x1a')](_0x23c5b8);
				return _0x57f079 + '-' + _0x179590;
			});
			var _0x39f10a = document['getElementById'](_0x2463('0x10'));
			_0x39f10a[_0x2463('0x0')] = 0x64;
			new Chart(_0x39f10a, {
				'type': _0x2463('0x14'),
				'data': {
					'labels': _0x53619a,
					'datasets': [{
						'label': _0x2463('0xe'),
						'borderColor': '#6456FF',
						'borderWidth': '2',
						'backgroundColor': _0x2463('0x18'),
						'pointBackgroundColor': _0x2463('0x8'),
						'data': _0x5775ae
					}, {
						'label': 'Death',
						'borderColor': _0x2463('0x1c'),
						'borderWidth': '2',
						'backgroundColor': 'transparent',
						'pointBackgroundColor': _0x2463('0x1c'),
						'data': _0x40dde8
					}, {
						'label': _0x2463('0x4'),
						'borderColor': _0x2463('0x17'),
						'borderWidth': '2',
						'backgroundColor': _0x2463('0x18'),
						'pointBackgroundColor': _0x2463('0x17'),
						'data': _0x491129
					}]
				},
				'options': {
					'responsive': !![],
					'maintainAspectRatio': ![],
					'legend': {
						'display': !![],
						'position': 'top',
						'labels': {
							'usePointStyle': !![]
						}
					},
					'tooltips': {
						'mode': _0x2463('0x3'),
						'intersect': ![]
					},
					'hover': {
						'mode': _0x2463('0x1'),
						'intersect': !![]
					},
					'scales': {
						'xAxes': [{
							'display': !![],
							'gridLines': {
								'display': !![],
								'drawBorder': ![],
								'color': _0x2463('0x9')
							},
							'scaleLabel': {
								'display': ![],
								'labelString': _0x2463('0x1e')
							}
						}],
						'yAxes': [{
							'display': !![],
							'gridLines': {
								'display': !![],
								'drawBorder': ![],
								'color': '#F7F8FC'
							},
							'scaleLabel': {
								'display': !![],
								'labelString': _0x2463('0x15')
							}
						}]
					}
				}
			});
		}
	});
});