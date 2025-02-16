var dom = document.getElementById("chart-panel");
                var myChart = echarts.init(dom);
                var option;
                var app ={};
                
option = {
    grid: {
        show: false,
        left: '5%',
        right: '70%',
        bottom: '5%',
        top: '10%',
        containLabel: true,
    },
    backgroundColor: 'transparent',
    xAxis: {
        show: false,
        type: 'value',
        max: 100,
    },
    tooltip:{
          show:true,
          formatter: '{b}:{c}%'
    },
    yAxis: 
        {
            type: 'category',
            inverse: true,
            axisLabel: {
                show: true,
                textStyle: {
                    fontSize: '12',
                    color: '#03fcfe',
                },
            },
            splitLine: {
                show: false,
            },
            axisTick: {
                show: false,
            },
            axisLine: {
                show: false,
            },
            data: ['完成进度'],
        },
       
    series: [
        {
            type: 'bar',
            showBackground: true,
            backgroundStyle: {
                   color: 'rgba(5, 4, 0, 0.537)',
                   borderRadius:20
            },
            label:{
                show:true,
                position:'right',
                distance: 0,
                formatter:'{insideTopRight|▲}{Right|{@[0]}%}',
                rich: {
                  Right: {
                  color: '03fcfe',
                  //width: 0,     
                  fontSize: '13',// 3  
                  verticalAlign:'middle'
                  },
                  insideTopRight: {
                  color: 'white',
                  align: 'right'  ,
                  width: 0,            
                  verticalAlign: "bottom",
                  lineHeight: 30 ,
                  fontSize: '10'
                  }
                }
            },
            
            itemStyle: {
                normal: {
                    barBorderRadius: 20,
                    color: new echarts.graphic.LinearGradient(1, 0, 0, 0, [
                        {
                            offset: 0,
                            color: '#1badf9',
                        },
                        {
                            offset: 1,
                            color: '#03fcfe',
                        },
                    ]),
                },
            },
            barWidth: 5,
            data: [50]
        },
    ],
};


                if (option && typeof option === 'object') {
                    myChart.setOption(option);
                }