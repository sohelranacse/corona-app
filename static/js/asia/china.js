var _0x4547 = ['#F7F8FC', 'recovered', 'China', '#6456FF', 'transparent', 'Month', 'Value', '#2DCE99', 'Confirmed', 'top', 'GET', 'formatToParts', 'date', 'DateTimeFormat', 'confirmed', 'nearest', 'json', 'numeric', 'height', 'deaths', 'getElementById', 'line', '#F5385A', 'china_timeseries', 'map', 'short', 'max', 'length', 'slice', 'Recovered', 'Death'];
(function (_0x1fdde3, _0x454750) {
	var _0x566f73 = function (_0x5477a5) {
		while (--_0x5477a5) {
			_0x1fdde3['push'](_0x1fdde3['shift']());
		}
	};
	_0x566f73(++_0x454750);
}(_0x4547, 0xe9));
var _0x566f = function (_0x1fdde3, _0x454750) {
	_0x1fdde3 = _0x1fdde3 - 0x0;
	var _0x566f73 = _0x4547[_0x1fdde3];
	return _0x566f73;
};
$(function () {
	$['ajax']({
		'type': _0x566f('0x19'),
		'url': 'https://pomber.github.io/covid19/timeseries.json',
		'dataType': _0x566f('0x0'),
		'success': function (_0x9821b6) {
			var _0x1a48f2 = _0x9821b6[_0x566f('0x11')][_0x566f('0xc')](Math[_0x566f('0xa')](_0x9821b6['China'][_0x566f('0xb')] - 0x1e, 0x1))[_0x566f('0x8')](_0x186be5 => _0x186be5[_0x566f('0x1d')]);
			var _0x208ee1 = _0x9821b6[_0x566f('0x11')][_0x566f('0xc')](Math[_0x566f('0xa')](_0x9821b6['China']['length'] - 0x1e, 0x1))[_0x566f('0x8')](_0x12e751 => _0x12e751[_0x566f('0x3')]);
			var _0x22de0e = _0x9821b6[_0x566f('0x11')][_0x566f('0xc')](Math['max'](_0x9821b6[_0x566f('0x11')][_0x566f('0xb')] - 0x1e, 0x1))[_0x566f('0x8')](_0x236027 => _0x236027[_0x566f('0x10')]);
			var _0x543b7c = _0x9821b6[_0x566f('0x11')][_0x566f('0xc')](Math[_0x566f('0xa')](_0x9821b6[_0x566f('0x11')]['length'] - 0x1e, 0x1))[_0x566f('0x8')](function (_0x4540f3) {
				const _0x907dac = new Date(_0x4540f3[_0x566f('0x1b')]);
				const _0x13ce8e = new Intl[(_0x566f('0x1c'))]('en', {
					'year': _0x566f('0x1'),
					'month': _0x566f('0x9'),
					'day': '2-digit'
				});
				const [{
					value: _0x2d5825
				}, , {
					value: _0x295cc5
				}] = _0x13ce8e[_0x566f('0x1a')](_0x907dac);
				return _0x295cc5 + '-' + _0x2d5825;
			});
			var _0xe20c08 = document[_0x566f('0x4')](_0x566f('0x7'));
			_0xe20c08[_0x566f('0x2')] = 0x64;
			new Chart(_0xe20c08, {
				'type': _0x566f('0x5'),
				'data': {
					'labels': _0x543b7c,
					'datasets': [{
						'label': _0x566f('0x17'),
						'borderColor': '#6456FF',
						'borderWidth': '2',
						'backgroundColor': 'transparent',
						'pointBackgroundColor': _0x566f('0x12'),
						'data': _0x1a48f2
					}, {
						'label': _0x566f('0xe'),
						'borderColor': '#F5385A',
						'borderWidth': '2',
						'backgroundColor': _0x566f('0x13'),
						'pointBackgroundColor': _0x566f('0x6'),
						'data': _0x208ee1
					}, {
						'label': _0x566f('0xd'),
						'borderColor': '#2DCE99',
						'borderWidth': '2',
						'backgroundColor': 'transparent',
						'pointBackgroundColor': _0x566f('0x16'),
						'data': _0x22de0e
					}]
				},
				'options': {
					'responsive': !![],
					'maintainAspectRatio': ![],
					'legend': {
						'display': !![],
						'position': _0x566f('0x18'),
						'labels': {
							'usePointStyle': !![]
						}
					},
					'tooltips': {
						'mode': 'index',
						'intersect': ![]
					},
					'hover': {
						'mode': _0x566f('0x1e'),
						'intersect': !![]
					},
					'scales': {
						'xAxes': [{
							'display': !![],
							'gridLines': {
								'display': !![],
								'drawBorder': ![],
								'color': _0x566f('0xf')
							},
							'scaleLabel': {
								'display': ![],
								'labelString': _0x566f('0x14')
							}
						}],
						'yAxes': [{
							'display': !![],
							'gridLines': {
								'display': !![],
								'drawBorder': ![],
								'color': _0x566f('0xf')
							},
							'scaleLabel': {
								'display': !![],
								'labelString': _0x566f('0x15')
							}
						}]
					}
				}
			});
		}
	});
});