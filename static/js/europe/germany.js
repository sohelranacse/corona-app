var _0x3d28 = ['numeric', 'formatToParts', 'transparent', '#2DCE99', 'Month', 'Death', 'short', 'index', 'Recovered', '#F7F8FC', 'Germany', 'confirmed', 'height', 'DateTimeFormat', 'ajax', 'nearest', 'https://pomber.github.io/covid19/timeseries.json', 'slice', '#6456FF', 'recovered', 'max', 'Confirmed', 'deaths', '2-digit', '#F5385A', 'map', 'line', 'date', 'length'];
(function (_0x3d02af, _0x3d28c2) {
	var _0x5b22c0 = function (_0x362970) {
		while (--_0x362970) {
			_0x3d02af['push'](_0x3d02af['shift']());
		}
	};
	_0x5b22c0(++_0x3d28c2);
}(_0x3d28, 0x164));
var _0x5b22 = function (_0x3d02af, _0x3d28c2) {
	_0x3d02af = _0x3d02af - 0x0;
	var _0x5b22c0 = _0x3d28[_0x3d02af];
	return _0x5b22c0;
};
$(function () {
	$[_0x5b22('0x6')]({
		'type': 'GET',
		'url': _0x5b22('0x8'),
		'dataType': 'json',
		'success': function (_0x5b8f44) {
			var _0x12a402 = _0x5b8f44[_0x5b22('0x2')][_0x5b22('0x9')](Math[_0x5b22('0xc')](_0x5b8f44[_0x5b22('0x2')][_0x5b22('0x14')] - 0x1e, 0x1))[_0x5b22('0x11')](_0x5988ae => _0x5988ae[_0x5b22('0x3')]);
			var _0x57eb9d = _0x5b8f44[_0x5b22('0x2')][_0x5b22('0x9')](Math[_0x5b22('0xc')](_0x5b8f44[_0x5b22('0x2')][_0x5b22('0x14')] - 0x1e, 0x1))['map'](_0x59e143 => _0x59e143[_0x5b22('0xe')]);
			var _0x2379c8 = _0x5b8f44[_0x5b22('0x2')][_0x5b22('0x9')](Math['max'](_0x5b8f44[_0x5b22('0x2')][_0x5b22('0x14')] - 0x1e, 0x1))[_0x5b22('0x11')](_0x90f427 => _0x90f427[_0x5b22('0xb')]);
			var _0x3cf6a7 = _0x5b8f44['Germany'][_0x5b22('0x9')](Math[_0x5b22('0xc')](_0x5b8f44[_0x5b22('0x2')]['length'] - 0x1e, 0x1))[_0x5b22('0x11')](function (_0x15df66) {
				const _0x2462c8 = new Date(_0x15df66[_0x5b22('0x13')]);
				const _0x47ad08 = new Intl[(_0x5b22('0x5'))]('en', {
					'year': _0x5b22('0x15'),
					'month': _0x5b22('0x1b'),
					'day': _0x5b22('0xf')
				});
				const [{
					value: _0x36c0dd
				}, , {
					value: _0x11432a
				}] = _0x47ad08[_0x5b22('0x16')](_0x2462c8);
				return _0x11432a + '-' + _0x36c0dd;
			});
			var _0x3c101b = document['getElementById']('germany_timeseries');
			_0x3c101b[_0x5b22('0x4')] = 0x64;
			new Chart(_0x3c101b, {
				'type': _0x5b22('0x12'),
				'data': {
					'labels': _0x3cf6a7,
					'datasets': [{
						'label': _0x5b22('0xd'),
						'borderColor': '#6456FF',
						'borderWidth': '2',
						'backgroundColor': _0x5b22('0x17'),
						'pointBackgroundColor': _0x5b22('0xa'),
						'data': _0x12a402
					}, {
						'label': _0x5b22('0x1a'),
						'borderColor': _0x5b22('0x10'),
						'borderWidth': '2',
						'backgroundColor': 'transparent',
						'pointBackgroundColor': _0x5b22('0x10'),
						'data': _0x57eb9d
					}, {
						'label': _0x5b22('0x0'),
						'borderColor': _0x5b22('0x18'),
						'borderWidth': '2',
						'backgroundColor': _0x5b22('0x17'),
						'pointBackgroundColor': _0x5b22('0x18'),
						'data': _0x2379c8
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
						'mode': _0x5b22('0x1c'),
						'intersect': ![]
					},
					'hover': {
						'mode': _0x5b22('0x7'),
						'intersect': !![]
					},
					'scales': {
						'xAxes': [{
							'display': !![],
							'gridLines': {
								'display': !![],
								'drawBorder': ![],
								'color': _0x5b22('0x1')
							},
							'scaleLabel': {
								'display': ![],
								'labelString': _0x5b22('0x19')
							}
						}],
						'yAxes': [{
							'display': !![],
							'gridLines': {
								'display': !![],
								'drawBorder': ![],
								'color': _0x5b22('0x1')
							},
							'scaleLabel': {
								'display': !![],
								'labelString': 'Value'
							}
						}]
					}
				}
			});
		}
	});
});