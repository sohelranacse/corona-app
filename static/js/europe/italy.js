var _0x10de = ['italy_timeseries', 'top', '#F7F8FC', '#6456FF', 'GET', 'transparent', 'Recovered', '#2DCE99', 'date', '#F5385A', 'numeric', 'recovered', 'map', 'formatToParts', 'https://api.covid19api.com/countries', 'max', 'Confirmed', 'Death', 'slice', 'ajax', 'short', 'https://pomber.github.io/covid19/timeseries.json', 'index', 'line', 'Italy', 'json', 'confirmed', 'height', 'length', 'deaths', '2-digit', 'nearest', 'log'];
(function (_0x1d9408, _0x10dea0) {
	var _0x4a70cc = function (_0x5c7e34) {
		while (--_0x5c7e34) {
			_0x1d9408['push'](_0x1d9408['shift']());
		}
	};
	_0x4a70cc(++_0x10dea0);
}(_0x10de, 0xe0));
var _0x4a70 = function (_0x1d9408, _0x10dea0) {
	_0x1d9408 = _0x1d9408 - 0x0;
	var _0x4a70cc = _0x10de[_0x1d9408];
	return _0x4a70cc;
};
$(function () {
	$['ajax']({
		'type': 'GET',
		'url': _0x4a70('0x1c'),
		'dataType': _0x4a70('0x20'),
		'success': function (_0x2caba2) {
			var _0xdab3f6 = _0x2caba2[_0x4a70('0x1f')][_0x4a70('0x19')](Math[_0x4a70('0x16')](_0x2caba2[_0x4a70('0x1f')][_0x4a70('0x2')] - 0x1e, 0x1))[_0x4a70('0x13')](_0x27e060 => _0x27e060[_0x4a70('0x0')]);
			var _0xb81447 = _0x2caba2[_0x4a70('0x1f')][_0x4a70('0x19')](Math[_0x4a70('0x16')](_0x2caba2['Italy'][_0x4a70('0x2')] - 0x1e, 0x1))[_0x4a70('0x13')](_0x1a31c0 => _0x1a31c0[_0x4a70('0x3')]);
			var _0x10ae1c = _0x2caba2[_0x4a70('0x1f')][_0x4a70('0x19')](Math[_0x4a70('0x16')](_0x2caba2['Italy'][_0x4a70('0x2')] - 0x1e, 0x1))[_0x4a70('0x13')](_0x346de5 => _0x346de5[_0x4a70('0x12')]);
			var _0x3a039f = _0x2caba2[_0x4a70('0x1f')][_0x4a70('0x19')](Math[_0x4a70('0x16')](_0x2caba2['Italy'][_0x4a70('0x2')] - 0x1e, 0x1))[_0x4a70('0x13')](function (_0x446bcf) {
				const _0x4faa56 = new Date(_0x446bcf[_0x4a70('0xf')]);
				const _0x11a54d = new Intl['DateTimeFormat']('en', {
					'year': _0x4a70('0x11'),
					'month': _0x4a70('0x1b'),
					'day': _0x4a70('0x4')
				});
				const [{
					value: _0x49cf2f
				}, , {
					value: _0x7cf71d
				}] = _0x11a54d[_0x4a70('0x14')](_0x4faa56);
				return _0x7cf71d + '-' + _0x49cf2f;
			});
			var _0x34cdcb = document['getElementById'](_0x4a70('0x7'));
			_0x34cdcb[_0x4a70('0x1')] = 0x64;
			new Chart(_0x34cdcb, {
				'type': _0x4a70('0x1e'),
				'data': {
					'labels': _0x3a039f,
					'datasets': [{
						'label': _0x4a70('0x17'),
						'borderColor': _0x4a70('0xa'),
						'borderWidth': '2',
						'backgroundColor': _0x4a70('0xc'),
						'pointBackgroundColor': _0x4a70('0xa'),
						'data': _0xdab3f6
					}, {
						'label': _0x4a70('0x18'),
						'borderColor': _0x4a70('0x10'),
						'borderWidth': '2',
						'backgroundColor': 'transparent',
						'pointBackgroundColor': _0x4a70('0x10'),
						'data': _0xb81447
					}, {
						'label': _0x4a70('0xd'),
						'borderColor': _0x4a70('0xe'),
						'borderWidth': '2',
						'backgroundColor': _0x4a70('0xc'),
						'pointBackgroundColor': _0x4a70('0xe'),
						'data': _0x10ae1c
					}]
				},
				'options': {
					'responsive': !![],
					'maintainAspectRatio': ![],
					'legend': {
						'display': !![],
						'position': _0x4a70('0x8'),
						'labels': {
							'usePointStyle': !![]
						}
					},
					'tooltips': {
						'mode': _0x4a70('0x1d'),
						'intersect': ![]
					},
					'hover': {
						'mode': _0x4a70('0x5'),
						'intersect': !![]
					},
					'scales': {
						'xAxes': [{
							'display': !![],
							'gridLines': {
								'display': !![],
								'drawBorder': ![],
								'color': _0x4a70('0x9')
							},
							'scaleLabel': {
								'display': ![],
								'labelString': 'Month'
							}
						}],
						'yAxes': [{
							'display': !![],
							'gridLines': {
								'display': !![],
								'drawBorder': ![],
								'color': _0x4a70('0x9')
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
$(function () {
	$[_0x4a70('0x1a')]({
		'type': _0x4a70('0xb'),
		'url': _0x4a70('0x15'),
		'dataType': _0x4a70('0x20'),
		'success': function (_0x22bbbd) {
			console[_0x4a70('0x6')](_0x22bbbd);
		}
	});
});