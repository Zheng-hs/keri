from flask import Flask, request, jsonify
import json
from flask_cors import CORS
from sqlalchemy import true

app = Flask(__name__)
CORS(app)


@app.route('/getMapInfo', methods=['GET', 'POST'])
def getMapInfoq():
    args = request.get_data()
    print(args)
    ret = {
        "data": {
            "mapInfoList": [
                {
                    "currentPoint": "10130",
                    "map_x": 39725,
                    "map_y": -57750,
                    "map_z": 0,
                    "targetPoint": [
                        "10129",
                        "10131"
                    ]
                },
                {
                    "currentPoint": "10217",
                    "map_x": 51250,
                    "map_y": -41000,
                    "map_z": 0,
                    "targetPoint": [
                        "10216",
                        "10218"
                    ]
                },
                {
                    "currentPoint": "10216",
                    "map_x": 51250,
                    "map_y": -40000,
                    "map_z": 0,
                    "targetPoint": [
                        "10215",
                        "10217"
                    ]
                },
                {
                    "currentPoint": "10139",
                    "map_x": 39775,
                    "map_y": -69250,
                    "map_z": 0,
                    "targetPoint": [
                        "10138",
                        "11901",
                        "11801"
                    ]
                },
                {
                    "currentPoint": "10219",
                    "map_x": 51250,
                    "map_y": -43250,
                    "map_z": 0,
                    "targetPoint": [
                        "10220",
                        "10218"
                    ]
                },
                {
                    "currentPoint": "11902",
                    "map_x": 29750,
                    "map_y": -69250,
                    "map_z": 0,
                    "targetPoint": [
                        "11901",
                        "11903"
                    ]
                },
                {
                    "currentPoint": "10218",
                    "map_x": 51250,
                    "map_y": -42000,
                    "map_z": 0,
                    "targetPoint": [
                        "10219",
                        "10217"
                    ]
                },
                {
                    "currentPoint": "11901",
                    "map_x": 34750,
                    "map_y": -69250,
                    "map_z": 0,
                    "targetPoint": [
                        "11902",
                        "10139"
                    ]
                },
                {
                    "currentPoint": "11904",
                    "map_x": 19750,
                    "map_y": -69250,
                    "map_z": 0,
                    "targetPoint": [
                        "11905",
                        "11903"
                    ]
                },
                {
                    "currentPoint": "11903",
                    "map_x": 24750,
                    "map_y": -69250,
                    "map_z": 0,
                    "targetPoint": [
                        "11902",
                        "11904"
                    ]
                },
                {
                    "currentPoint": "11906",
                    "map_x": 7500,
                    "map_y": -61250,
                    "map_z": 0,
                    "targetPoint": [
                        "11905",
                        "11907"
                    ]
                },
                {
                    "currentPoint": "11905",
                    "map_x": 7500,
                    "map_y": -69250,
                    "map_z": 0,
                    "targetPoint": [
                        "11906",
                        "11904"
                    ]
                },
                {
                    "currentPoint": "10132",
                    "map_x": 39725,
                    "map_y": -60000,
                    "map_z": 0,
                    "targetPoint": [
                        "10133",
                        "10131"
                    ]
                },
                {
                    "currentPoint": "10131",
                    "map_x": 39725,
                    "map_y": -59000,
                    "map_z": 0,
                    "targetPoint": [
                        "10132",
                        "10130"
                    ]
                },
                {
                    "currentPoint": "10134",
                    "map_x": 39725,
                    "map_y": -62500,
                    "map_z": 0,
                    "targetPoint": [
                        "10133",
                        "10135"
                    ]
                },
                {
                    "currentPoint": "10211",
                    "map_x": 51250,
                    "map_y": -33750,
                    "map_z": 0,
                    "targetPoint": [
                        "10210",
                        "10212"
                    ]
                },
                {
                    "currentPoint": "10210",
                    "map_x": 51250,
                    "map_y": -32500,
                    "map_z": 0,
                    "targetPoint": [
                        "10211",
                        "10209"
                    ]
                },
                {
                    "currentPoint": "10133",
                    "map_x": 39725,
                    "map_y": -61250,
                    "map_z": 0,
                    "targetPoint": [
                        "10132",
                        "10134"
                    ]
                },
                {
                    "currentPoint": "10136",
                    "map_x": 39725,
                    "map_y": -65000,
                    "map_z": 0,
                    "targetPoint": [
                        "10135",
                        "10137"
                    ]
                },
                {
                    "currentPoint": "10213",
                    "map_x": 51250,
                    "map_y": -36500,
                    "map_z": 0,
                    "targetPoint": [
                        "10212",
                        "10214"
                    ]
                },
                {
                    "currentPoint": "10135",
                    "map_x": 39725,
                    "map_y": -63750,
                    "map_z": 0,
                    "targetPoint": [
                        "10134",
                        "10136"
                    ]
                },
                {
                    "currentPoint": "10212",
                    "map_x": 51250,
                    "map_y": -35500,
                    "map_z": 0,
                    "targetPoint": [
                        "10213",
                        "10211"
                    ]
                },
                {
                    "currentPoint": "10215",
                    "map_x": 51250,
                    "map_y": -38750,
                    "map_z": 0,
                    "targetPoint": [
                        "10216",
                        "10214"
                    ]
                },
                {
                    "currentPoint": "10138",
                    "map_x": 39725,
                    "map_y": -67500,
                    "map_z": 0,
                    "targetPoint": [
                        "10137",
                        "10139"
                    ]
                },
                {
                    "currentPoint": "10137",
                    "map_x": 39725,
                    "map_y": -66500,
                    "map_z": 0,
                    "targetPoint": [
                        "10138",
                        "10136"
                    ]
                },
                {
                    "currentPoint": "10214",
                    "map_x": 51250,
                    "map_y": -37500,
                    "map_z": 0,
                    "targetPoint": [
                        "10213",
                        "10215"
                    ]
                },
                {
                    "currentPoint": "11908",
                    "map_x": 9750,
                    "map_y": -57750,
                    "map_z": 0,
                    "targetPoint": [
                        "11909",
                        "11907"
                    ]
                },
                {
                    "currentPoint": "11907",
                    "map_x": 7500,
                    "map_y": -57750,
                    "map_z": 0,
                    "targetPoint": [
                        "11906",
                        "11908"
                    ]
                },
                {
                    "currentPoint": "11909",
                    "map_x": 11250,
                    "map_y": -57750,
                    "map_z": 0,
                    "targetPoint": [
                        "11908",
                        "11910"
                    ]
                },
                {
                    "currentPoint": "10107",
                    "map_x": 39725,
                    "map_y": -29000,
                    "map_z": 0,
                    "targetPoint": [
                        "10108",
                        "10106"
                    ]
                },
                {
                    "currentPoint": "10228",
                    "map_x": 51250,
                    "map_y": -55000,
                    "map_z": 0,
                    "targetPoint": [
                        "10227",
                        "10229"
                    ]
                },
                {
                    "currentPoint": "11910",
                    "map_x": 13250,
                    "map_y": -57750,
                    "map_z": 0,
                    "targetPoint": [
                        "11909"
                    ]
                },
                {
                    "currentPoint": "10106",
                    "map_x": 39725,
                    "map_y": -27250,
                    "map_z": 0,
                    "targetPoint": [
                        "10105",
                        "10107"
                    ]
                },
                {
                    "currentPoint": "10227",
                    "map_x": 51250,
                    "map_y": -53750,
                    "map_z": 0,
                    "targetPoint": [
                        "10226",
                        "10228"
                    ]
                },
                {
                    "currentPoint": "10109",
                    "map_x": 39725,
                    "map_y": -31500,
                    "map_z": 0,
                    "targetPoint": [
                        "10108",
                        "10110"
                    ]
                },
                {
                    "currentPoint": "10229",
                    "map_x": 51250,
                    "map_y": -56250,
                    "map_z": 0,
                    "targetPoint": [
                        "10230",
                        "10228"
                    ]
                },
                {
                    "currentPoint": "10108",
                    "map_x": 39725,
                    "map_y": -30500,
                    "map_z": 0,
                    "targetPoint": [
                        "10109",
                        "10107"
                    ]
                },
                {
                    "currentPoint": "10220",
                    "map_x": 51250,
                    "map_y": -44750,
                    "map_z": 0,
                    "targetPoint": [
                        "10221",
                        "10219"
                    ]
                },
                {
                    "currentPoint": "10222",
                    "map_x": 51250,
                    "map_y": -47000,
                    "map_z": 0,
                    "targetPoint": [
                        "10221",
                        "10223"
                    ]
                },
                {
                    "currentPoint": "10101",
                    "map_x": 39725,
                    "map_y": -20500,
                    "map_z": 0,
                    "targetPoint": [
                        "10102"
                    ]
                },
                {
                    "currentPoint": "10221",
                    "map_x": 51250,
                    "map_y": -46000,
                    "map_z": 0,
                    "targetPoint": [
                        "10220",
                        "10222"
                    ]
                },
                {
                    "currentPoint": "10103",
                    "map_x": 39725,
                    "map_y": -23750,
                    "map_z": 0,
                    "targetPoint": [
                        "10104",
                        "10102"
                    ]
                },
                {
                    "currentPoint": "10224",
                    "map_x": 51250,
                    "map_y": -50000,
                    "map_z": 0,
                    "targetPoint": [
                        "10225",
                        "10223"
                    ]
                },
                {
                    "currentPoint": "10102",
                    "map_x": 39725,
                    "map_y": -22750,
                    "map_z": 0,
                    "targetPoint": [
                        "10103",
                        "10101"
                    ]
                },
                {
                    "currentPoint": "10223",
                    "map_x": 51250,
                    "map_y": -48250,
                    "map_z": 0,
                    "targetPoint": [
                        "10222",
                        "10224"
                    ]
                },
                {
                    "currentPoint": "10105",
                    "map_x": 39725,
                    "map_y": -26250,
                    "map_z": 0,
                    "targetPoint": [
                        "10104",
                        "10106"
                    ]
                },
                {
                    "currentPoint": "10226",
                    "map_x": 51250,
                    "map_y": -52500,
                    "map_z": 0,
                    "targetPoint": [
                        "10225",
                        "10227"
                    ]
                },
                {
                    "currentPoint": "10225",
                    "map_x": 51250,
                    "map_y": -51250,
                    "map_z": 0,
                    "targetPoint": [
                        "10226",
                        "10224"
                    ]
                },
                {
                    "currentPoint": "10104",
                    "map_x": 39725,
                    "map_y": -24750,
                    "map_z": 0,
                    "targetPoint": [
                        "10105",
                        "10103"
                    ]
                },
                {
                    "currentPoint": "10239",
                    "map_x": 51225,
                    "map_y": -69250,
                    "map_z": 0,
                    "targetPoint": [
                        "11802",
                        "10238"
                    ]
                },
                {
                    "currentPoint": "10118",
                    "map_x": 39725,
                    "map_y": -42250,
                    "map_z": 0,
                    "targetPoint": [
                        "10117",
                        "10119"
                    ]
                },
                {
                    "currentPoint": "11801",
                    "map_x": 44750,
                    "map_y": -69250,
                    "map_z": 0,
                    "targetPoint": [
                        "11802",
                        "10139"
                    ]
                },
                {
                    "currentPoint": "10238",
                    "map_x": 51250,
                    "map_y": -67250,
                    "map_z": 0,
                    "targetPoint": [
                        "10239",
                        "10237"
                    ]
                },
                {
                    "currentPoint": "10117",
                    "map_x": 39725,
                    "map_y": -41250,
                    "map_z": 0,
                    "targetPoint": [
                        "10118",
                        "10116"
                    ]
                },
                {
                    "currentPoint": "10119",
                    "map_x": 39725,
                    "map_y": -43500,
                    "map_z": 0,
                    "targetPoint": [
                        "10120",
                        "10118"
                    ]
                },
                {
                    "currentPoint": "11802",
                    "map_x": 48250,
                    "map_y": -69250,
                    "map_z": 0,
                    "targetPoint": [
                        "10239",
                        "11801"
                    ]
                },
                {
                    "currentPoint": "10110",
                    "map_x": 39725,
                    "map_y": -32750,
                    "map_z": 0,
                    "targetPoint": [
                        "10111",
                        "10109"
                    ]
                },
                {
                    "currentPoint": "10231",
                    "map_x": 51250,
                    "map_y": -58750,
                    "map_z": 0,
                    "targetPoint": [
                        "10232",
                        "10230"
                    ]
                },
                {
                    "currentPoint": "10230",
                    "map_x": 51250,
                    "map_y": -57500,
                    "map_z": 0,
                    "targetPoint": [
                        "10229",
                        "10231"
                    ]
                },
                {
                    "currentPoint": "10112",
                    "map_x": 39725,
                    "map_y": -35750,
                    "map_z": 0,
                    "targetPoint": [
                        "10113",
                        "10111"
                    ]
                },
                {
                    "currentPoint": "10233",
                    "map_x": 51250,
                    "map_y": -61000,
                    "map_z": 0,
                    "targetPoint": [
                        "10234",
                        "10232"
                    ]
                },
                {
                    "currentPoint": "10111",
                    "map_x": 39725,
                    "map_y": -34000,
                    "map_z": 0,
                    "targetPoint": [
                        "10112",
                        "10110"
                    ]
                },
                {
                    "currentPoint": "10232",
                    "map_x": 51250,
                    "map_y": -59750,
                    "map_z": 0,
                    "targetPoint": [
                        "10233",
                        "10231"
                    ]
                },
                {
                    "currentPoint": "10114",
                    "map_x": 39725,
                    "map_y": -37750,
                    "map_z": 0,
                    "targetPoint": [
                        "10113",
                        "10115"
                    ]
                },
                {
                    "currentPoint": "10235",
                    "map_x": 51250,
                    "map_y": -63500,
                    "map_z": 0,
                    "targetPoint": [
                        "10234",
                        "10236"
                    ]
                },
                {
                    "currentPoint": "10234",
                    "map_x": 51250,
                    "map_y": -62250,
                    "map_z": 0,
                    "targetPoint": [
                        "10235",
                        "10233"
                    ]
                },
                {
                    "currentPoint": "10113",
                    "map_x": 39725,
                    "map_y": -36750,
                    "map_z": 0,
                    "targetPoint": [
                        "10112",
                        "10114"
                    ]
                },
                {
                    "currentPoint": "10116",
                    "map_x": 39725,
                    "map_y": -40250,
                    "map_z": 0,
                    "targetPoint": [
                        "10117",
                        "10115"
                    ]
                },
                {
                    "currentPoint": "10237",
                    "map_x": 51250,
                    "map_y": -66250,
                    "map_z": 0,
                    "targetPoint": [
                        "10236",
                        "10238"
                    ]
                },
                {
                    "currentPoint": "10236",
                    "map_x": 51250,
                    "map_y": -64750,
                    "map_z": 0,
                    "targetPoint": [
                        "10235",
                        "10237"
                    ]
                },
                {
                    "currentPoint": "10115",
                    "map_x": 39725,
                    "map_y": -39000,
                    "map_z": 0,
                    "targetPoint": [
                        "10116",
                        "10114"
                    ]
                },
                {
                    "currentPoint": "10129",
                    "map_x": 39725,
                    "map_y": -56750,
                    "map_z": 0,
                    "targetPoint": [
                        "10130",
                        "10128"
                    ]
                },
                {
                    "currentPoint": "10206",
                    "map_x": 51250,
                    "map_y": -27000,
                    "map_z": 0,
                    "targetPoint": [
                        "10207",
                        "10205"
                    ]
                },
                {
                    "currentPoint": "10205",
                    "map_x": 51250,
                    "map_y": -26000,
                    "map_z": 0,
                    "targetPoint": [
                        "10206",
                        "10204"
                    ]
                },
                {
                    "currentPoint": "10128",
                    "map_x": 39725,
                    "map_y": -55250,
                    "map_z": 0,
                    "targetPoint": [
                        "10127",
                        "10129"
                    ]
                },
                {
                    "currentPoint": "10208",
                    "map_x": 51250,
                    "map_y": -30250,
                    "map_z": 0,
                    "targetPoint": [
                        "10207",
                        "10209"
                    ]
                },
                {
                    "currentPoint": "10207",
                    "map_x": 51250,
                    "map_y": -28750,
                    "map_z": 0,
                    "targetPoint": [
                        "10206",
                        "10208"
                    ]
                },
                {
                    "currentPoint": "10209",
                    "map_x": 51250,
                    "map_y": -31250,
                    "map_z": 0,
                    "targetPoint": [
                        "10208",
                        "10210"
                    ]
                },
                {
                    "currentPoint": "10121",
                    "map_x": 39725,
                    "map_y": -46250,
                    "map_z": 0,
                    "targetPoint": [
                        "10120",
                        "10122"
                    ]
                },
                {
                    "currentPoint": "10120",
                    "map_x": 39725,
                    "map_y": -45000,
                    "map_z": 0,
                    "targetPoint": [
                        "10121",
                        "10119"
                    ]
                },
                {
                    "currentPoint": "10123",
                    "map_x": 39725,
                    "map_y": -48500,
                    "map_z": 0,
                    "targetPoint": [
                        "10122",
                        "10124"
                    ]
                },
                {
                    "currentPoint": "10122",
                    "map_x": 39725,
                    "map_y": -47250,
                    "map_z": 0,
                    "targetPoint": [
                        "10121",
                        "10123"
                    ]
                },
                {
                    "currentPoint": "10202",
                    "map_x": 51250,
                    "map_y": -22500,
                    "map_z": 0,
                    "targetPoint": [
                        "10203",
                        "10201"
                    ]
                },
                {
                    "currentPoint": "10125",
                    "map_x": 39725,
                    "map_y": -51500,
                    "map_z": 0,
                    "targetPoint": [
                        "10126",
                        "10124"
                    ]
                },
                {
                    "currentPoint": "10201",
                    "map_x": 51250,
                    "map_y": -20250,
                    "map_z": 0,
                    "targetPoint": [
                        "10202"
                    ]
                },
                {
                    "currentPoint": "10124",
                    "map_x": 39725,
                    "map_y": -50250,
                    "map_z": 0,
                    "targetPoint": [
                        "10125",
                        "10123"
                    ]
                },
                {
                    "currentPoint": "10127",
                    "map_x": 39725,
                    "map_y": -54000,
                    "map_z": 0,
                    "targetPoint": [
                        "10128",
                        "10126"
                    ]
                },
                {
                    "currentPoint": "10204",
                    "map_x": 51250,
                    "map_y": -24500,
                    "map_z": 0,
                    "targetPoint": [
                        "10205",
                        "10203"
                    ]
                },
                {
                    "currentPoint": "10126",
                    "map_x": 39725,
                    "map_y": -52750,
                    "map_z": 0,
                    "targetPoint": [
                        "10125",
                        "10127"
                    ]
                },
                {
                    "currentPoint": "10203",
                    "map_x": 51250,
                    "map_y": -23500,
                    "map_z": 0,
                    "targetPoint": [
                        "10204",
                        "10202"
                    ]
                },
                {
                    "currentPoint": "Point-0001",
                    "map_x": 0,
                    "map_y": 0,
                    "map_z": 0,
                    "targetPoint": []
                },
                {
                    "currentPoint": "Point-0002",
                    "map_x": 817750,
                    "map_y": -482500,
                    "map_z": 0,
                    "targetPoint": []
                }
            ]
        },
        "meta": {
            "msg": "返回成功",
            "status": 200
        }
    }

    return ret


@app.route('/getMapInfo1', methods=['GET', 'POST'])
def getMapInfo():
    args = request.get_data()
    print(args)
    ret = {
        "data": {
            "mapInfoList": [
                {
                    "currentPoint": 'Point-0001',
                    "map_x": 0,
                    "map_y": -113000.0,
                    "map_z": 0.0,
                    "targetPoint": []
                },
                {
                    "currentPoint": 'Point-0002',
                    "map_x": 109250.0,
                    "map_y": 27000.0,
                    "map_z": 0.0,
                    "targetPoint": []
                },
                {
                    "currentPoint": '907',
                    "map_x": 51700,
                    "map_y": -21200,
                    "targetPoint": ['908', '906']
                },
                {
                    "currentPoint": '908',
                    "map_x": 51700,
                    "map_y": -22600,
                    "targetPoint": ['909', '907'],
                },
                {
                    "currentPoint": '909',
                    "map_x": 51800,
                    "map_y": -18800,
                    "targetPoint": ['908', '910'],
                },
                {
                    "currentPoint": '1220',
                    "map_x": 64800,
                    "map_y": -22500,
                    "targetPoint": ['1221', '1219'],
                },
                {
                    "currentPoint": '1217',
                    "map_x": 64700,
                    "map_y": -18700,
                    "targetPoint": ['1216', '1218'],
                },
                {
                    "currentPoint": '1216',
                    "map_x": 64800,
                    "map_y": -22500,
                    "targetPoint": ['1215', '1217'],
                },
                {
                    "currentPoint": '1215',
                    "map_x": 64800,
                    "map_y": -21200,
                    "targetPoint": ['1214', '1216'],
                },
                {
                    "currentPoint": '1214',
                    "map_x": 64700,
                    "map_y": -20100,
                    "targetPoint": ['1215', '1213'],
                },
                {
                    "currentPoint": '1213',
                    "map_x": 64700,
                    "map_y": -18700,
                    "targetPoint": ['1214', '1212'],
                },
                {
                    "currentPoint": '1212',
                    "map_x": 64800,
                    "map_y": -22500,
                    "targetPoint": ['1213', '1211'],
                },
                {
                    "currentPoint": '1211',
                    "map_x": 64800,
                    "map_y": -21200,
                    "targetPoint": ['1210', '1212'],
                },
                {
                    "currentPoint": '1332',
                    "map_x": 70300,
                    "map_y": -22400,
                    "targetPoint": ['48', '1331'],
                },
                {
                    "currentPoint": '1210',
                    "map_x": 64700,
                    "map_y": -20100,
                    "targetPoint": ['1209', '1211'],
                },
                {
                    "currentPoint": '1331',
                    "map_x": 70300,
                    "map_y": -21000,
                    "targetPoint": ['1332', '1330'],
                },
                {
                    "currentPoint": '910',
                    "map_x": 51700,
                    "map_y": -20000,
                    "targetPoint": ['909', '911'],
                },
                {
                    "currentPoint": '911',
                    "map_x": 51700,
                    "map_y": -21200,
                    "targetPoint": ['910', '912'],
                },
                {
                    "currentPoint": '912',
                    "map_x": 51700,
                    "map_y": -22600,
                    "targetPoint": ['911', '913'],
                },
                {
                    "currentPoint": '913',
                    "map_x": 51800,
                    "map_y": -18800,
                    "targetPoint": ['914', '912'],
                },
                {
                    "currentPoint": '914',
                    "map_x": 51700,
                    "map_y": -20000,
                    "targetPoint": ['915', '913'],
                },
                {
                    "currentPoint": '915',
                    "map_x": 51700,
                    "map_y": -21200,
                    "targetPoint": ['914', '916'],
                },
                {
                    "currentPoint": '916',
                    "map_x": 51700,
                    "map_y": -22600,
                    "targetPoint": ['917', '915'],
                },
                {
                    "currentPoint": '1219',
                    "map_x": 64800,
                    "map_y": -21200,
                    "targetPoint": ['1218', '1220'],
                },
                {
                    "currentPoint": '1218',
                    "map_x": 64700,
                    "map_y": -20100,
                    "targetPoint": ['1219', '1217'],
                },
                {
                    "currentPoint": '917',
                    "map_x": 51800,
                    "map_y": -18800,
                    "targetPoint": ['918', '916'],
                },
                {
                    "currentPoint": '918',
                    "map_x": 51700,
                    "map_y": -20000,
                    "targetPoint": ['917', '919'],
                },
                {
                    "currentPoint": '919',
                    "map_x": 51700,
                    "map_y": -21200,
                    "targetPoint": ['920', '918'],
                },
                {
                    "currentPoint": '1110',
                    "map_x": 59900,
                    "map_y": -20100,
                    "targetPoint": ['1109', '1111'],
                },
                {
                    "currentPoint": '1231',
                    "map_x": 64800,
                    "map_y": -21200,
                    "targetPoint": ['1232', '1239'],
                },
                {
                    "currentPoint": '1228',
                    "map_x": 64800,
                    "map_y": -22500,
                    "targetPoint": ['1227', '1229'],
                },
                {
                    "currentPoint": '1107',
                    "map_x": 59900,
                    "map_y": -21500,
                    "targetPoint": ['1108', '1106'],
                },
                {
                    "currentPoint": '1106',
                    "map_x": 59900,
                    "map_y": -20100,
                    "targetPoint": ['1105', '1107'],
                },
                {
                    "currentPoint": '1227',
                    "map_x": 64800,
                    "map_y": -21200,
                    "targetPoint": ['1228', '1226'],
                },
                {
                    "currentPoint": '1105',
                    "map_x": 59800,
                    "map_y": -18600,
                    "targetPoint": ['1104', '1106'],
                },
                {
                    "currentPoint": '1226',
                    "map_x": 64700,
                    "map_y": -20100,
                    "targetPoint": ['1227', '1225'],
                },
                {
                    "currentPoint": '1225',
                    "map_x": 64700,
                    "map_y": -18700,
                    "targetPoint": ['1226', '1224'],
                },
                {
                    "currentPoint": '1104',
                    "map_x": 60000,
                    "map_y": -22900,
                    "targetPoint": ['1103', '1105'],
                },
                {
                    "currentPoint": '1103',
                    "map_x": 59900,
                    "map_y": -21500,
                    "targetPoint": ['1104', '1102'],
                },
                {
                    "currentPoint": '1224',
                    "map_x": 64800,
                    "map_y": -22500,
                    "targetPoint": ['1223', '1225'],
                },
                {
                    "currentPoint": '1102',
                    "map_x": 59900,
                    "map_y": -20100,
                    "targetPoint": ['1103', '1101'],
                },
                {
                    "currentPoint": '1223',
                    "map_x": 64800,
                    "map_y": -21200,
                    "targetPoint": ['1222', '1224'],
                },
                {
                    "currentPoint": '1222',
                    "map_x": 64700,
                    "map_y": -20100,
                    "targetPoint": ['1221', '1223'],
                },
                {
                    "currentPoint": '1101',
                    "map_x": 59800,
                    "map_y": -18600,
                    "targetPoint": ['1102', '1100'],
                },
                {
                    "currentPoint": '920',
                    "map_x": 51700,
                    "map_y": -22600,
                    "targetPoint": ['919', '921'],
                },
                {
                    "currentPoint": '1100',
                    "map_x": 59800,
                    "map_y": -15500,
                    "targetPoint": ['1101'],
                },
                {
                    "currentPoint": '1221',
                    "map_x": 64700,
                    "map_y": -18700,
                    "targetPoint": ['1222', '1220'],
                },
                {
                    "currentPoint": '921',
                    "map_x": 51800,
                    "map_y": -18800,
                    "targetPoint": ['922', '920'],
                },
                {
                    "currentPoint": '800',
                    "map_x": 44100,
                    "map_y": -15600,
                    "targetPoint": ['801'],
                },
                {
                    "currentPoint": '801',
                    "map_x": 43100,
                    "map_y": -15700,
                    "targetPoint": ['802', '800'],
                },
                {
                    "currentPoint": '922',
                    "map_x": 51700,
                    "map_y": -20000,
                    "targetPoint": ['921', '923'],
                },
                {
                    "currentPoint": '802',
                    "map_x": 47200,
                    "map_y": -19700,
                    "targetPoint": ['803', '801'],
                },
                {
                    "currentPoint": '923',
                    "map_x": 51700,
                    "map_y": -21200,
                    "targetPoint": ['924', '922'],
                },
                {
                    "currentPoint": '924',
                    "map_x": 51700,
                    "map_y": -22600,
                    "targetPoint": ['925', '923'],
                },
                {
                    "currentPoint": '803',
                    "map_x": 47200,
                    "map_y": -20700,
                    "targetPoint": ['802', '804'],
                },
                {
                    "currentPoint": '925',
                    "map_x": 51800,
                    "map_y": -18800,
                    "targetPoint": ['924', '926'],
                },
                {
                    "currentPoint": '804',
                    "map_x": 47200,
                    "map_y": -21800,
                    "targetPoint": ['803', '805'],
                },
                {
                    "currentPoint": '805',
                    "map_x": 43100,
                    "map_y": -15700,
                    "targetPoint": ['806', '804'],
                },
                {
                    "currentPoint": '926',
                    "map_x": 51700,
                    "map_y": -20000,
                    "targetPoint": ['925', '927'],
                },
                {
                    "currentPoint": '927',
                    "map_x": 51700,
                    "map_y": -21200,
                    "targetPoint": ['926', '928'],
                },
                {
                    "currentPoint": '806',
                    "map_x": 47200,
                    "map_y": -19700,
                    "targetPoint": ['805', '807'],
                },
                {
                    "currentPoint": '1109',
                    "map_x": 59800,
                    "map_y": -18600,
                    "targetPoint": ['1108', '1110'],
                },
                {
                    "currentPoint": '1108',
                    "map_x": 60000,
                    "map_y": -22900,
                    "targetPoint": ['1109', '1107'],
                },
                {
                    "currentPoint": '928',
                    "map_x": 51700,
                    "map_y": -22600,
                    "targetPoint": ['929', '927'],
                },
                {
                    "currentPoint": '807',
                    "map_x": 47200,
                    "map_y": -20700,
                    "targetPoint": ['806', '808'],
                },
                {
                    "currentPoint": '1229',
                    "map_x": 64700,
                    "map_y": -18700,
                    "targetPoint": ['1228', '1239'],
                },
                {
                    "currentPoint": '808',
                    "map_x": 47200,
                    "map_y": -21800,
                    "targetPoint": ['809', '807'],
                },
                {
                    "currentPoint": '929',
                    "map_x": 51800,
                    "map_y": -18800,
                    "targetPoint": ['930', '928'],
                },
                {
                    "currentPoint": '809',
                    "map_x": 43100,
                    "map_y": -15700,
                    "targetPoint": ['810', '808'],
                },
                {
                    "currentPoint": '1000',
                    "map_x": 56500,
                    "map_y": -15600,
                    "targetPoint": ['1001'],
                },
                {
                    "currentPoint": '1121',
                    "map_x": 59800,
                    "map_y": -18600,
                    "targetPoint": ['1122', '1120'],
                },
                {
                    "currentPoint": '1120',
                    "map_x": 60000,
                    "map_y": -22900,
                    "targetPoint": ['1121', '1119'],
                },
                {
                    "currentPoint": '1118',
                    "map_x": 59900,
                    "map_y": -20100,
                    "targetPoint": ['1117', '1119'],
                },
                {
                    "currentPoint": '1239',
                    "map_x": 64700,
                    "map_y": -20100,
                    "targetPoint": ['1231', '1229'],
                },
                {
                    "currentPoint": '1117',
                    "map_x": 59800,
                    "map_y": -18600,
                    "targetPoint": ['1116', '1118'],
                },
                {
                    "currentPoint": '1116',
                    "map_x": 60000,
                    "map_y": -22900,
                    "targetPoint": ['1115', '1117'],
                },
                {
                    "currentPoint": '1115',
                    "map_x": 59900,
                    "map_y": -21500,
                    "targetPoint": ['1116', '1114'],
                },
                {
                    "currentPoint": '1114',
                    "map_x": 59900,
                    "map_y": -20100,
                    "targetPoint": ['1115', '1113'],
                },
                {
                    "currentPoint": '1113',
                    "map_x": 59800,
                    "map_y": -18600,
                    "targetPoint": ['1112', '1114'],
                },
                {
                    "currentPoint": '1112',
                    "map_x": 60000,
                    "map_y": -22900,
                    "targetPoint": ['1111', '1113'],
                },
                {
                    "currentPoint": '930',
                    "map_x": 51700,
                    "map_y": -20000,
                    "targetPoint": ['931', '929'],
                },
                {
                    "currentPoint": '1232',
                    "map_x": 64800,
                    "map_y": -22500,
                    "targetPoint": ['1231', '46'],
                },
                {
                    "currentPoint": '931',
                    "map_x": 51700,
                    "map_y": -21200,
                    "targetPoint": ['930', '932'],
                },
                {
                    "currentPoint": '1111',
                    "map_x": 59900,
                    "map_y": -21500,
                    "targetPoint": ['1110', '1112'],
                },
                {
                    "currentPoint": '810',
                    "map_x": 47200,
                    "map_y": -19700,
                    "targetPoint": ['811', '809'],
                },
                {
                    "currentPoint": '932',
                    "map_x": 51700,
                    "map_y": -22600,
                    "targetPoint": ['43', '931'],
                },
                {
                    "currentPoint": '811',
                    "map_x": 47200,
                    "map_y": -20700,
                    "targetPoint": ['810', '812'],
                },
                {
                    "currentPoint": '812',
                    "map_x": 47200,
                    "map_y": -21800,
                    "targetPoint": ['811', '813'],
                },
                {
                    "currentPoint": '813',
                    "map_x": 43100,
                    "map_y": -15700,
                    "targetPoint": ['812', '814'],
                },
                {
                    "currentPoint": '814',
                    "map_x": 47200,
                    "map_y": -19700,
                    "targetPoint": ['815', '813'],
                },
                {
                    "currentPoint": '815',
                    "map_x": 47200,
                    "map_y": -20700,
                    "targetPoint": ['816', '814'],
                },
                {
                    "currentPoint": '816',
                    "map_x": 47200,
                    "map_y": -21800,
                    "targetPoint": ['815', '817'],
                },
                {
                    "currentPoint": '817',
                    "map_x": 43100,
                    "map_y": -15700,
                    "targetPoint": ['818', '816'],
                },
                {
                    "currentPoint": '818',
                    "map_x": 47200,
                    "map_y": -19700,
                    "targetPoint": ['819', '817'],
                },
                {
                    "currentPoint": '1119',
                    "map_x": 59900,
                    "map_y": -21500,
                    "targetPoint": ['1120', '1118'],
                },
                {
                    "currentPoint": '819',
                    "map_x": 47200,
                    "map_y": -20700,
                    "targetPoint": ['818', '820'],
                },
                {
                    "currentPoint": '1132',
                    "map_x": 60000,
                    "map_y": -22900,
                    "targetPoint": ['45', '1131'],
                },
                {
                    "currentPoint": '1011',
                    "map_x": 56500,
                    "map_y": -21000,
                    "targetPoint": ['1012', '1010'],
                },
                {
                    "currentPoint": '1131',
                    "map_x": 59900,
                    "map_y": -21500,
                    "targetPoint": ['1130', '1132'],
                },
                {
                    "currentPoint": '1010',
                    "map_x": 56500,
                    "map_y": -19800,
                    "targetPoint": ['1009', '1011'],
                },
                {
                    "currentPoint": '1130',
                    "map_x": 59900,
                    "map_y": -20100,
                    "targetPoint": ['1131', '1129'],
                },
                {
                    "currentPoint": '1008',
                    "map_x": 56500,
                    "map_y": -22300,
                    "targetPoint": ['1009', '1007'],
                },
                {
                    "currentPoint": '1129',
                    "map_x": 59800,
                    "map_y": -18600,
                    "targetPoint": ['1130', '1128'],
                },
                {
                    "currentPoint": '1128',
                    "map_x": 60000,
                    "map_y": -22900,
                    "targetPoint": ['1129', '1127'],
                },
                {
                    "currentPoint": '1007',
                    "map_x": 56500,
                    "map_y": -21000,
                    "targetPoint": ['1006', '1008'],
                },
                {
                    "currentPoint": '1127',
                    "map_x": 59900,
                    "map_y": -21500,
                    "targetPoint": ['1128', '1126'],
                },
                {
                    "currentPoint": '1006',
                    "map_x": 56500,
                    "map_y": -19800,
                    "targetPoint": ['1005', '1007'],
                },
                {
                    "currentPoint": '1005',
                    "map_x": 56500,
                    "map_y": -18700,
                    "targetPoint": ['1004', '1006'],
                },
                {
                    "currentPoint": '1126',
                    "map_x": 59900,
                    "map_y": -20100,
                    "targetPoint": ['1127', '1125'],
                },
                {
                    "currentPoint": '1125',
                    "map_x": 59800,
                    "map_y": -18600,
                    "targetPoint": ['1124', '1126'],
                },
                {
                    "currentPoint": '1004',
                    "map_x": 56500,
                    "map_y": -22300,
                    "targetPoint": ['1005', '1003'],
                },
                {
                    "currentPoint": '1003',
                    "map_x": 56500,
                    "map_y": -21000,
                    "targetPoint": ['1004', '1002'],
                },
                {
                    "currentPoint": '1124',
                    "map_x": 60000,
                    "map_y": -22900,
                    "targetPoint": ['1123', '1125'],
                },
                {
                    "currentPoint": '820',
                    "map_x": 47200,
                    "map_y": -21800,
                    "targetPoint": ['819', '821'],
                },
                {
                    "currentPoint": '1123',
                    "map_x": 59900,
                    "map_y": -21500,
                    "targetPoint": ['1122', '1124'],
                },
                {
                    "currentPoint": '1002',
                    "map_x": 56500,
                    "map_y": -19800,
                    "targetPoint": ['1003', '1001'],
                },
                {
                    "currentPoint": '1001',
                    "map_x": 56500,
                    "map_y": -18700,
                    "targetPoint": ['1000', '1002'],
                },
                {
                    "currentPoint": '700',
                    "map_x": 36500,
                    "map_y": -15700,
                    "targetPoint": ['701'],
                },
                {
                    "currentPoint": '1122',
                    "map_x": 59900,
                    "map_y": -20100,
                    "targetPoint": ['1123', '1121'],
                },
                {
                    "currentPoint": '821',
                    "map_x": 43100,
                    "map_y": -15700,
                    "targetPoint": ['820', '822'],
                },
                {
                    "currentPoint": '822',
                    "map_x": 47200,
                    "map_y": -19700,
                    "targetPoint": ['823', '821'],
                },
                {
                    "currentPoint": '701',
                    "map_x": 41100,
                    "map_y": -15600,
                    "targetPoint": ['702', '700'],
                },
                {
                    "currentPoint": '702',
                    "map_x": 44200,
                    "map_y": -19800,
                    "targetPoint": ['701', '703'],
                },
                {
                    "currentPoint": '823',
                    "map_x": 47200,
                    "map_y": -20700,
                    "targetPoint": ['824', '822'],
                },
                {
                    "currentPoint": '703',
                    "map_x": 44200,
                    "map_y": -20900,
                    "targetPoint": ['704', '702'],
                },
                {
                    "currentPoint": '824',
                    "map_x": 47200,
                    "map_y": -21800,
                    "targetPoint": ['825', '823'],
                },
                {
                    "currentPoint": '825',
                    "map_x": 43100,
                    "map_y": -15700,
                    "targetPoint": ['824', '826'],
                },
                {
                    "currentPoint": '704',
                    "map_x": 44200,
                    "map_y": -21900,
                    "targetPoint": ['705', '703'],
                },
                {
                    "currentPoint": '826',
                    "map_x": 47200,
                    "map_y": -19700,
                    "targetPoint": ['825', '827'],
                },
                {
                    "currentPoint": '705',
                    "map_x": 41100,
                    "map_y": -15600,
                    "targetPoint": ['704', '706'],
                },
                {
                    "currentPoint": '706',
                    "map_x": 44200,
                    "map_y": -19800,
                    "targetPoint": ['707', '705'],
                },
                {
                    "currentPoint": '827',
                    "map_x": 47200,
                    "map_y": -20700,
                    "targetPoint": ['826', '828'],
                },
                {
                    "currentPoint": '707',
                    "map_x": 44200,
                    "map_y": -20900,
                    "targetPoint": ['706', '708'],
                },
                {
                    "currentPoint": '828',
                    "map_x": 47200,
                    "map_y": -21800,
                    "targetPoint": ['827', '829'],
                },
                {
                    "currentPoint": '1009',
                    "map_x": 56500,
                    "map_y": -18700,
                    "targetPoint": ['1008', '1010'],
                },
                {
                    "currentPoint": '829',
                    "map_x": 43100,
                    "map_y": -15700,
                    "targetPoint": ['828', '830'],
                },
                {
                    "currentPoint": '708',
                    "map_x": 44200,
                    "map_y": -21900,
                    "targetPoint": ['707', '709'],
                },
                {
                    "currentPoint": '709',
                    "map_x": 41100,
                    "map_y": -15600,
                    "targetPoint": ['708', '710'],
                },
                {
                    "currentPoint": '1022',
                    "map_x": 56500,
                    "map_y": -19800,
                    "targetPoint": ['1023', '1021'],
                },
                {
                    "currentPoint": '1021',
                    "map_x": 56500,
                    "map_y": -18700,
                    "targetPoint": ['1022', '1020'],
                },
                {
                    "currentPoint": '1020',
                    "map_x": 56500,
                    "map_y": -22300,
                    "targetPoint": ['1019', '1021'],
                },
                {
                    "currentPoint": '1019',
                    "map_x": 56500,
                    "map_y": -21000,
                    "targetPoint": ['1020', '1018'],
                },
                {
                    "currentPoint": '1018',
                    "map_x": 56500,
                    "map_y": -19800,
                    "targetPoint": ['1017', '1019'],
                },
                {
                    "currentPoint": '1017',
                    "map_x": 56500,
                    "map_y": -18700,
                    "targetPoint": ['1018', '1016'],
                },
                {
                    "currentPoint": '1016',
                    "map_x": 56500,
                    "map_y": -22300,
                    "targetPoint": ['1017', '1015'],
                },
                {
                    "currentPoint": '1015',
                    "map_x": 56500,
                    "map_y": -21000,
                    "targetPoint": ['1016', '1014'],
                },
                {
                    "currentPoint": '830',
                    "map_x": 47200,
                    "map_y": -19700,
                    "targetPoint": ['829', '831'],
                },
                {
                    "currentPoint": '1014',
                    "map_x": 56500,
                    "map_y": -19800,
                    "targetPoint": ['1013', '1015'],
                },
                {
                    "currentPoint": '831',
                    "map_x": 47200,
                    "map_y": -20700,
                    "targetPoint": ['832', '830'],
                },
                {
                    "currentPoint": '1013',
                    "map_x": 56500,
                    "map_y": -18700,
                    "targetPoint": ['1012', '1014'],
                },
                {
                    "currentPoint": '710',
                    "map_x": 44200,
                    "map_y": -19800,
                    "targetPoint": ['711', '709'],
                },
                {
                    "currentPoint": '1012',
                    "map_x": 56500,
                    "map_y": -22300,
                    "targetPoint": ['1011', '1013'],
                },
                {
                    "currentPoint": '711',
                    "map_x": 44200,
                    "map_y": -20900,
                    "targetPoint": ['712', '710'],
                },
                {
                    "currentPoint": '832',
                    "map_x": 47200,
                    "map_y": -21800,
                    "targetPoint": ['831', '42'],
                },
                {
                    "currentPoint": '712',
                    "map_x": 44200,
                    "map_y": -21900,
                    "targetPoint": ['711', '713'],
                },
                {
                    "currentPoint": '713',
                    "map_x": 41100,
                    "map_y": -15600,
                    "targetPoint": ['714', '712'],
                },
                {
                    "currentPoint": '714',
                    "map_x": 44200,
                    "map_y": -19800,
                    "targetPoint": ['713', '715'],
                },
                {
                    "currentPoint": '715',
                    "map_x": 44200,
                    "map_y": -20900,
                    "targetPoint": ['716', '714'],
                },
                {
                    "currentPoint": '716',
                    "map_x": 44200,
                    "map_y": -21900,
                    "targetPoint": ['717', '715'],
                },
                {
                    "currentPoint": '717',
                    "map_x": 41100,
                    "map_y": -15600,
                    "targetPoint": ['716', '718'],
                },
                {
                    "currentPoint": '718',
                    "map_x": 44200,
                    "map_y": -19800,
                    "targetPoint": ['719', '717'],
                },
                {
                    "currentPoint": '719',
                    "map_x": 44200,
                    "map_y": -20900,
                    "targetPoint": ['718', '720'],
                },
                {
                    "currentPoint": '1032',
                    "map_x": 56500,
                    "map_y": -22300,
                    "targetPoint": ['1031', '44'],
                },
                {
                    "currentPoint": '1031',
                    "map_x": 56500,
                    "map_y": -21000,
                    "targetPoint": ['1030', '1032'],
                },
                {
                    "currentPoint": '1030',
                    "map_x": 56500,
                    "map_y": -19800,
                    "targetPoint": ['1031', '1029'],
                },
                {
                    "currentPoint": '1029',
                    "map_x": 56500,
                    "map_y": -18700,
                    "targetPoint": ['1030', '1028'],
                },
                {
                    "currentPoint": '1028',
                    "map_x": 56500,
                    "map_y": -22300,
                    "targetPoint": ['1029', '1027'],
                },
                {
                    "currentPoint": '1027',
                    "map_x": 56500,
                    "map_y": -21000,
                    "targetPoint": ['1028', '1026'],
                },
                {
                    "currentPoint": '1026',
                    "map_x": 56500,
                    "map_y": -19800,
                    "targetPoint": ['1025', '1027'],
                },
                {
                    "currentPoint": '1025',
                    "map_x": 56500,
                    "map_y": -18700,
                    "targetPoint": ['1024', '1026'],
                },
                {
                    "currentPoint": '720',
                    "map_x": 44200,
                    "map_y": -21900,
                    "targetPoint": ['719', '721'],
                },
                {
                    "currentPoint": '721',
                    "map_x": 41100,
                    "map_y": -15600,
                    "targetPoint": ['720', '722'],
                },
                {
                    "currentPoint": '1024',
                    "map_x": 56500,
                    "map_y": -22300,
                    "targetPoint": ['1023', '1025'],
                },
                {
                    "currentPoint": '600',
                    "map_x": 41100,
                    "map_y": -15600,
                    "targetPoint": ['601'],
                },
                {
                    "currentPoint": '601',
                    "map_x": 41100,
                    "map_y": -18700,
                    "targetPoint": ['602', '600'],
                },
                {
                    "currentPoint": '722',
                    "map_x": 44200,
                    "map_y": -19800,
                    "targetPoint": ['721', '723'],
                },
                {
                    "currentPoint": '1023',
                    "map_x": 56500,
                    "map_y": -21000,
                    "targetPoint": ['1024', '1022'],
                },
                {
                    "currentPoint": '723',
                    "map_x": 44200,
                    "map_y": -20900,
                    "targetPoint": ['724', '722'],
                },
                {
                    "currentPoint": '602',
                    "map_x": 41100,
                    "map_y": -20000,
                    "targetPoint": ['603', '601'],
                },
                {
                    "currentPoint": '603',
                    "map_x": 41200,
                    "map_y": -21100,
                    "targetPoint": ['602', '604'],
                },
                {
                    "currentPoint": '724',
                    "map_x": 44200,
                    "map_y": -21900,
                    "targetPoint": ['725', '723'],
                },
                {
                    "currentPoint": '604',
                    "map_x": 41200,
                    "map_y": -22500,
                    "targetPoint": ['605', '603'],
                },
                {
                    "currentPoint": '725',
                    "map_x": 41100,
                    "map_y": -15600,
                    "targetPoint": ['726', '724'],
                },
                {
                    "currentPoint": '726',
                    "map_x": 44200,
                    "map_y": -19800,
                    "targetPoint": ['725', '727'],
                },
                {
                    "currentPoint": '605',
                    "map_x": 41100,
                    "map_y": -18700,
                    "targetPoint": ['606', '604'],
                },
                {
                    "currentPoint": '727',
                    "map_x": 44200,
                    "map_y": -20900,
                    "targetPoint": ['728', '726'],
                },
                {
                    "currentPoint": '606',
                    "map_x": 41100,
                    "map_y": -20000,
                    "targetPoint": ['607', '605'],
                },
                {
                    "currentPoint": '728',
                    "map_x": 44200,
                    "map_y": -21900,
                    "targetPoint": ['727', '729'],
                },
                {
                    "currentPoint": '607',
                    "map_x": 41200,
                    "map_y": -21100,
                    "targetPoint": ['608', '606'],
                },
                {
                    "currentPoint": '608',
                    "map_x": 41200,
                    "map_y": -22500,
                    "targetPoint": ['607', '609'],
                },
                {
                    "currentPoint": '729',
                    "map_x": 41100,
                    "map_y": -15600,
                    "targetPoint": ['728', '730'],
                },
                {
                    "currentPoint": '609',
                    "map_x": 41100,
                    "map_y": -18700,
                    "targetPoint": ['610', '608'],
                },
                {
                    "currentPoint": '730',
                    "map_x": 44200,
                    "map_y": -19800,
                    "targetPoint": ['729', '731'],
                },
                {
                    "currentPoint": '731',
                    "map_x": 44200,
                    "map_y": -20900,
                    "targetPoint": ['732', '730'],
                },
                {
                    "currentPoint": '610',
                    "map_x": 41100,
                    "map_y": -20000,
                    "targetPoint": ['611', '609'],
                },
                {
                    "currentPoint": '732',
                    "map_x": 44200,
                    "map_y": -21900,
                    "targetPoint": ['41', '731'],
                },
                {
                    "currentPoint": '611',
                    "map_x": 41200,
                    "map_y": -21100,
                    "targetPoint": ['612', '610'],
                },
                {
                    "currentPoint": '612',
                    "map_x": 41200,
                    "map_y": -22500,
                    "targetPoint": ['611', '613'],
                },
                {
                    "currentPoint": '613',
                    "map_x": 41100,
                    "map_y": -18700,
                    "targetPoint": ['612', '614'],
                },
                {
                    "currentPoint": '614',
                    "map_x": 41100,
                    "map_y": -20000,
                    "targetPoint": ['613', '615'],
                },
                {
                    "currentPoint": '615',
                    "map_x": 41200,
                    "map_y": -21100,
                    "targetPoint": ['614', '616'],
                },
                {
                    "currentPoint": '616',
                    "map_x": 41200,
                    "map_y": -22500,
                    "targetPoint": ['617', '615'],
                },
                {
                    "currentPoint": '617',
                    "map_x": 41100,
                    "map_y": -18700,
                    "targetPoint": ['616', '618'],
                },
                {
                    "currentPoint": '618',
                    "map_x": 41100,
                    "map_y": -20000,
                    "targetPoint": ['617', '619'],
                },
                {
                    "currentPoint": '619',
                    "map_x": 41200,
                    "map_y": -21100,
                    "targetPoint": ['620', '618'],
                },
                {
                    "currentPoint": '620',
                    "map_x": 41200,
                    "map_y": -22500,
                    "targetPoint": ['619', '621'],
                },
                {
                    "currentPoint": '621',
                    "map_x": 41100,
                    "map_y": -18700,
                    "targetPoint": ['620', '622'],
                },
                {
                    "currentPoint": '500',
                    "map_x": 36500,
                    "map_y": -15700,
                    "targetPoint": ['501'],
                },
                {
                    "currentPoint": '501',
                    "map_x": 36400,
                    "map_y": -18900,
                    "targetPoint": ['500', '502'],
                },
                {
                    "currentPoint": '622',
                    "map_x": 41100,
                    "map_y": -20000,
                    "targetPoint": ['621', '623'],
                },
                {
                    "currentPoint": '502',
                    "map_x": 36400,
                    "map_y": -20100,
                    "targetPoint": ['503', '501'],
                },
                {
                    "currentPoint": '623',
                    "map_x": 41200,
                    "map_y": -21100,
                    "targetPoint": ['622', '624'],
                },
                {
                    "currentPoint": '624',
                    "map_x": 41200,
                    "map_y": -22500,
                    "targetPoint": ['623', '625'],
                },
                {
                    "currentPoint": '503',
                    "map_x": 36400,
                    "map_y": -21400,
                    "targetPoint": ['502', '504'],
                },
                {
                    "currentPoint": '504',
                    "map_x": 36400,
                    "map_y": -22400,
                    "targetPoint": ['505', '503'],
                },
                {
                    "currentPoint": '625',
                    "map_x": 41100,
                    "map_y": -18700,
                    "targetPoint": ['624', '626'],
                },
                {
                    "currentPoint": '505',
                    "map_x": 36400,
                    "map_y": -18900,
                    "targetPoint": ['506', '504'],
                },
                {
                    "currentPoint": '626',
                    "map_x": 41100,
                    "map_y": -20000,
                    "targetPoint": ['627', '625'],
                },
                {
                    "currentPoint": '627',
                    "map_x": 41200,
                    "map_y": -21100,
                    "targetPoint": ['626', '628'],
                },
                {
                    "currentPoint": '506',
                    "map_x": 36400,
                    "map_y": -20100,
                    "targetPoint": ['507', '505'],
                },
                {
                    "currentPoint": '507',
                    "map_x": 36400,
                    "map_y": -21400,
                    "targetPoint": ['508', '506'],
                },
                {
                    "currentPoint": '628',
                    "map_x": 41200,
                    "map_y": -22500,
                    "targetPoint": ['629', '627'],
                },
                {
                    "currentPoint": '629',
                    "map_x": 41100,
                    "map_y": -18700,
                    "targetPoint": ['628', '630'],
                },
                {
                    "currentPoint": '508',
                    "map_x": 36400,
                    "map_y": -22400,
                    "targetPoint": ['509', '507'],
                },
                {
                    "currentPoint": '509',
                    "map_x": 36400,
                    "map_y": -18900,
                    "targetPoint": ['508', '510'],
                },
                {
                    "currentPoint": 'Point-0499',
                    "map_x": 74900,
                    "map_y": -19600,
                    "targetPoint": ['Point-0498', 'Point-0500'],
                },
                {
                    "currentPoint": 'Point-0498',
                    "map_x": 74900,
                    "map_y": -18600,
                    "targetPoint": ['Point-0497', 'Point-0499'],
                },
                {
                    "currentPoint": '630',
                    "map_x": 41100,
                    "map_y": -20000,
                    "targetPoint": ['631', '629'],
                },
                {
                    "currentPoint": '510',
                    "map_x": 36400,
                    "map_y": -20100,
                    "targetPoint": ['511', '509'],
                },
                {
                    "currentPoint": '631',
                    "map_x": 41200,
                    "map_y": -21100,
                    "targetPoint": ['632', '630'],
                },
                {
                    "currentPoint": '511',
                    "map_x": 36400,
                    "map_y": -21400,
                    "targetPoint": ['510', '512'],
                },
                {
                    "currentPoint": '632',
                    "map_x": 41200,
                    "map_y": -22500,
                    "targetPoint": ['40', '631'],
                },
                {
                    "currentPoint": '512',
                    "map_x": 36400,
                    "map_y": -22400,
                    "targetPoint": ['513', '511'],
                },
                {
                    "currentPoint": '513',
                    "map_x": 36400,
                    "map_y": -18900,
                    "targetPoint": ['512', '514'],
                },
                {
                    "currentPoint": '514',
                    "map_x": 36400,
                    "map_y": -20100,
                    "targetPoint": ['515', '513'],
                },
                {
                    "currentPoint": '515',
                    "map_x": 36400,
                    "map_y": -21400,
                    "targetPoint": ['516', '514'],
                },
                {
                    "currentPoint": '516',
                    "map_x": 36400,
                    "map_y": -22400,
                    "targetPoint": ['515', '517'],
                },
                {
                    "currentPoint": '517',
                    "map_x": 36400,
                    "map_y": -18900,
                    "targetPoint": ['518', '516'],
                },
                {
                    "currentPoint": '518',
                    "map_x": 36400,
                    "map_y": -20100,
                    "targetPoint": ['517', '519'],
                },
                {
                    "currentPoint": '519',
                    "map_x": 36400,
                    "map_y": -21400,
                    "targetPoint": ['520', '518'],
                },
                {
                    "currentPoint": '520',
                    "map_x": 36400,
                    "map_y": -22400,
                    "targetPoint": ['521', '519'],
                },
                {
                    "currentPoint": '400',
                    "map_x": 31600,
                    "map_y": -15700,
                    "targetPoint": ['401'],
                },
                {
                    "currentPoint": 'Point-0497',
                    "map_x": 70300,
                    "map_y": -15600,
                    "targetPoint": ['Point-0498'],
                },
                {
                    "currentPoint": '521',
                    "map_x": 36400,
                    "map_y": -18900,
                    "targetPoint": ['522', '520'],
                },
                {
                    "currentPoint": '522',
                    "map_x": 36400,
                    "map_y": -20100,
                    "targetPoint": ['521', '523'],
                },
                {
                    "currentPoint": '401',
                    "map_x": 31700,
                    "map_y": -18900,
                    "targetPoint": ['400', '402'],
                },
                {
                    "currentPoint": '523',
                    "map_x": 36400,
                    "map_y": -21400,
                    "targetPoint": ['522', '524'],
                },
                {
                    "currentPoint": '402',
                    "map_x": 31800,
                    "map_y": -20100,
                    "targetPoint": ['401', '403'],
                },
                {
                    "currentPoint": '403',
                    "map_x": 31800,
                    "map_y": -21200,
                    "targetPoint": ['404', '402'],
                },
                {
                    "currentPoint": '524',
                    "map_x": 36400,
                    "map_y": -22400,
                    "targetPoint": ['523', '525'],
                },
                {
                    "currentPoint": '525',
                    "map_x": 36400,
                    "map_y": -18900,
                    "targetPoint": ['524', '526'],
                },
                {
                    "currentPoint": '404',
                    "map_x": 31800,
                    "map_y": -22200,
                    "targetPoint": ['403', '405'],
                },
                {
                    "currentPoint": '405',
                    "map_x": 31700,
                    "map_y": -18900,
                    "targetPoint": ['406', '404'],
                },
                {
                    "currentPoint": '526',
                    "map_x": 36400,
                    "map_y": -20100,
                    "targetPoint": ['525', '527'],
                },
                {
                    "currentPoint": '527',
                    "map_x": 36400,
                    "map_y": -21400,
                    "targetPoint": ['528', '526'],
                },
                {
                    "currentPoint": '406',
                    "map_x": 31800,
                    "map_y": -20100,
                    "targetPoint": ['407', '405'],
                },
                {
                    "currentPoint": '528',
                    "map_x": 36400,
                    "map_y": -22400,
                    "targetPoint": ['527', '529'],
                },
                {
                    "currentPoint": '407',
                    "map_x": 31800,
                    "map_y": -21200,
                    "targetPoint": ['408', '406'],
                },
                {
                    "currentPoint": '408',
                    "map_x": 31800,
                    "map_y": -22200,
                    "targetPoint": ['409', '407'],
                },
                {
                    "currentPoint": '529',
                    "map_x": 36400,
                    "map_y": -18900,
                    "targetPoint": ['530', '528'],
                },
                {
                    "currentPoint": '409',
                    "map_x": 31700,
                    "map_y": -18900,
                    "targetPoint": ['408', '410'],
                },
                {
                    "currentPoint": 'Point-0599',
                    "map_x": 74900,
                    "map_y": -18600,
                    "targetPoint": ['Point-0600', 'Point-0534'],
                },
                {
                    "currentPoint": 'Point-0598',
                    "map_x": 75000,
                    "map_y": -22400,
                    "targetPoint": ['Point-0663', 'Point-0597'],
                },
                {
                    "currentPoint": 'Point-0597',
                    "map_x": 74900,
                    "map_y": -20900,
                    "targetPoint": ['Point-0596', 'Point-0598'],
                },
                {
                    "currentPoint": '530',
                    "map_x": 36400,
                    "map_y": -20100,
                    "targetPoint": ['529', '531'],
                },
                {
                    "currentPoint": '410',
                    "map_x": 31800,
                    "map_y": -20100,
                    "targetPoint": ['409', '411'],
                },
                {
                    "currentPoint": '531',
                    "map_x": 36400,
                    "map_y": -21400,
                    "targetPoint": ['532', '530'],
                },
                {
                    "currentPoint": '411',
                    "map_x": 31800,
                    "map_y": -21200,
                    "targetPoint": ['410', '412'],
                },
                {
                    "currentPoint": '532',
                    "map_x": 36400,
                    "map_y": -22400,
                    "targetPoint": ['531', '39'],
                },
                {
                    "currentPoint": '412',
                    "map_x": 31800,
                    "map_y": -22200,
                    "targetPoint": ['411', '413'],
                },
                {
                    "currentPoint": '413',
                    "map_x": 31700,
                    "map_y": -18900,
                    "targetPoint": ['414', '412'],
                },
                {
                    "currentPoint": '414',
                    "map_x": 31800,
                    "map_y": -20100,
                    "targetPoint": ['413', '415'],
                },
                {
                    "currentPoint": '415',
                    "map_x": 31800,
                    "map_y": -21200,
                    "targetPoint": ['416', '414'],
                },
                {
                    "currentPoint": '416',
                    "map_x": 31800,
                    "map_y": -22200,
                    "targetPoint": ['417', '415'],
                },
                {
                    "currentPoint": '417',
                    "map_x": 31700,
                    "map_y": -18900,
                    "targetPoint": ['416', '418'],
                },
                {
                    "currentPoint": '418',
                    "map_x": 31800,
                    "map_y": -20100,
                    "targetPoint": ['419', '417'],
                },
                {
                    "currentPoint": '419',
                    "map_x": 31800,
                    "map_y": -21200,
                    "targetPoint": ['420', '418'],
                },
                {
                    "currentPoint": 'Point-0589',
                    "map_x": 74900,
                    "map_y": -20900,
                    "targetPoint": ['Point-0590', 'Point-0588'],
                },
                {
                    "currentPoint": 'Point-0468',
                    "map_x": 75000,
                    "map_y": -22400,
                    "targetPoint": ['Point-0467', 'Point-0591'],
                },
                {
                    "currentPoint": 'Point-0467',
                    "map_x": 74900,
                    "map_y": -20900,
                    "targetPoint": ['Point-0466', 'Point-0468'],
                },
                {
                    "currentPoint": 'Point-0588',
                    "map_x": 74900,
                    "map_y": -19600,
                    "targetPoint": ['Point-0587', 'Point-0589'],
                },
                {
                    "currentPoint": 'Point-0587',
                    "map_x": 74900,
                    "map_y": -18600,
                    "targetPoint": ['Point-0588', 'Point-0435'],
                },
                {
                    "currentPoint": 'Point-0466',
                    "map_x": 74900,
                    "map_y": -19600,
                    "targetPoint": ['Point-0465', 'Point-0467'],
                },
                {
                    "currentPoint": 'Point-0465',
                    "map_x": 74900,
                    "map_y": -18600,
                    "targetPoint": ['Point-0466', 'Point-0464'],
                },
                {
                    "currentPoint": 'Point-0592',
                    "map_x": 74900,
                    "map_y": -19600,
                    "targetPoint": ['Point-0591', 'Point-0593'],
                },
                {
                    "currentPoint": 'Point-0591',
                    "map_x": 74900,
                    "map_y": -18600,
                    "targetPoint": ['Point-0592', 'Point-0468'],
                },
                {
                    "currentPoint": '420',
                    "map_x": 31800,
                    "map_y": -22200,
                    "targetPoint": ['419', '421'],
                },
                {
                    "currentPoint": 'Point-0590',
                    "map_x": 75000,
                    "map_y": -22400,
                    "targetPoint": ['Point-0589', 'Point-0655'],
                },
                {
                    "currentPoint": '300',
                    "map_x": 27100,
                    "map_y": -15700,
                    "targetPoint": ['301'],
                },
                {
                    "currentPoint": '421',
                    "map_x": 31700,
                    "map_y": -18900,
                    "targetPoint": ['422', '420'],
                },
                {
                    "currentPoint": '301',
                    "map_x": 27100,
                    "map_y": -19000,
                    "targetPoint": ['302', '300'],
                },
                {
                    "currentPoint": 'Point-0596',
                    "map_x": 74900,
                    "map_y": -19600,
                    "targetPoint": ['Point-0597', 'Point-0595'],
                },
                {
                    "currentPoint": '422',
                    "map_x": 31800,
                    "map_y": -20100,
                    "targetPoint": ['423', '421'],
                },
                {
                    "currentPoint": 'Point-0595',
                    "map_x": 74900,
                    "map_y": -18600,
                    "targetPoint": ['Point-0501', 'Point-0596'],
                },
                {
                    "currentPoint": '423',
                    "map_x": 31800,
                    "map_y": -21200,
                    "targetPoint": ['422', '424'],
                },
                {
                    "currentPoint": '302',
                    "map_x": 27100,
                    "map_y": -20100,
                    "targetPoint": ['301', '303'],
                },
                {
                    "currentPoint": '424',
                    "map_x": 31800,
                    "map_y": -22200,
                    "targetPoint": ['423', '425'],
                },
                {
                    "currentPoint": '303',
                    "map_x": 27100,
                    "map_y": -21200,
                    "targetPoint": ['302', '304'],
                },
                {
                    "currentPoint": 'Point-0594',
                    "map_x": 75000,
                    "map_y": -22400,
                    "targetPoint": ['Point-0593', 'Point-0659'],
                },
                {
                    "currentPoint": '304',
                    "map_x": 27100,
                    "map_y": -22400,
                    "targetPoint": ['305', '303'],
                },
                {
                    "currentPoint": '425',
                    "map_x": 31700,
                    "map_y": -18900,
                    "targetPoint": ['424', '426'],
                },
                {
                    "currentPoint": 'Point-0593',
                    "map_x": 74900,
                    "map_y": -20900,
                    "targetPoint": ['Point-0592', 'Point-0594'],
                },
                {
                    "currentPoint": '305',
                    "map_x": 27100,
                    "map_y": -19000,
                    "targetPoint": ['304', '306'],
                },
                {
                    "currentPoint": '426',
                    "map_x": 31800,
                    "map_y": -20100,
                    "targetPoint": ['425', '427'],
                },
                {
                    "currentPoint": '427',
                    "map_x": 31800,
                    "map_y": -21200,
                    "targetPoint": ['428', '426'],
                },
                {
                    "currentPoint": '306',
                    "map_x": 27100,
                    "map_y": -20100,
                    "targetPoint": ['305', '307'],
                },
                {
                    "currentPoint": '428',
                    "map_x": 31800,
                    "map_y": -22200,
                    "targetPoint": ['429', '427'],
                },
                {
                    "currentPoint": '307',
                    "map_x": 27100,
                    "map_y": -21200,
                    "targetPoint": ['308', '306'],
                },
                {
                    "currentPoint": '308',
                    "map_x": 27100,
                    "map_y": -22400,
                    "targetPoint": ['309', '307'],
                },
                {
                    "currentPoint": '429',
                    "map_x": 31700,
                    "map_y": -18900,
                    "targetPoint": ['430', '428'],
                },
                {
                    "currentPoint": '309',
                    "map_x": 27100,
                    "map_y": -19000,
                    "targetPoint": ['308', '310'],
                },
                {
                    "currentPoint": '430',
                    "map_x": 31800,
                    "map_y": -20100,
                    "targetPoint": ['429', '431'],
                },
                {
                    "currentPoint": '431',
                    "map_x": 31800,
                    "map_y": -21200,
                    "targetPoint": ['430', '432'],
                },
                {
                    "currentPoint": '310',
                    "map_x": 27100,
                    "map_y": -20100,
                    "targetPoint": ['311', '309'],
                },
                {
                    "currentPoint": '311',
                    "map_x": 27100,
                    "map_y": -21200,
                    "targetPoint": ['310', '312'],
                },
                {
                    "currentPoint": '432',
                    "map_x": 31800,
                    "map_y": -22200,
                    "targetPoint": ['431', '38'],
                },
                {
                    "currentPoint": '312',
                    "map_x": 27100,
                    "map_y": -22400,
                    "targetPoint": ['311', '313'],
                },
                {
                    "currentPoint": '313',
                    "map_x": 27100,
                    "map_y": -19000,
                    "targetPoint": ['312', '314'],
                },
                {
                    "currentPoint": '314',
                    "map_x": 27100,
                    "map_y": -20100,
                    "targetPoint": ['315', '313'],
                },
                {
                    "currentPoint": '315',
                    "map_x": 27100,
                    "map_y": -21200,
                    "targetPoint": ['314', '316'],
                },
                {
                    "currentPoint": '316',
                    "map_x": 27100,
                    "map_y": -22400,
                    "targetPoint": ['317', '315'],
                },
                {
                    "currentPoint": '317',
                    "map_x": 27100,
                    "map_y": -19000,
                    "targetPoint": ['318', '316'],
                },
                {
                    "currentPoint": '318',
                    "map_x": 27100,
                    "map_y": -20100,
                    "targetPoint": ['317', '319'],
                },
                {
                    "currentPoint": '319',
                    "map_x": 27100,
                    "map_y": -21200,
                    "targetPoint": ['318', '320'],
                },
                {
                    "currentPoint": '320',
                    "map_x": 27100,
                    "map_y": -22400,
                    "targetPoint": ['321', '319'],
                },
                {
                    "currentPoint": '200',
                    "map_x": 22300,
                    "map_y": -15700,
                    "targetPoint": ['201'],
                },
                {
                    "currentPoint": '321',
                    "map_x": 27100,
                    "map_y": -19000,
                    "targetPoint": ['322', '320'],
                },
                {
                    "currentPoint": '322',
                    "map_x": 27100,
                    "map_y": -20100,
                    "targetPoint": ['323', '321'],
                },
                {
                    "currentPoint": '201',
                    "map_x": 22500,
                    "map_y": -19300,
                    "targetPoint": ['200', '202'],
                },
                {
                    "currentPoint": '323',
                    "map_x": 27100,
                    "map_y": -21200,
                    "targetPoint": ['324', '322'],
                },
                {
                    "currentPoint": '202',
                    "map_x": 22500,
                    "map_y": -20300,
                    "targetPoint": ['203', '201'],
                },
                {
                    "currentPoint": '324',
                    "map_x": 27100,
                    "map_y": -22400,
                    "targetPoint": ['325', '323'],
                },
                {
                    "currentPoint": '203',
                    "map_x": 22500,
                    "map_y": -21300,
                    "targetPoint": ['202', '204'],
                },
                {
                    "currentPoint": '325',
                    "map_x": 27100,
                    "map_y": -19000,
                    "targetPoint": ['324', '326'],
                },
                {
                    "currentPoint": '204',
                    "map_x": 22500,
                    "map_y": -22300,
                    "targetPoint": ['203', '205'],
                },
                {
                    "currentPoint": '326',
                    "map_x": 27100,
                    "map_y": -20100,
                    "targetPoint": ['325', '327'],
                },
                {
                    "currentPoint": '205',
                    "map_x": 22500,
                    "map_y": -19300,
                    "targetPoint": ['206', '204'],
                },
                {
                    "currentPoint": '206',
                    "map_x": 22500,
                    "map_y": -20300,
                    "targetPoint": ['205', '207'],
                },
                {
                    "currentPoint": '327',
                    "map_x": 27100,
                    "map_y": -21200,
                    "targetPoint": ['326', '328'],
                },
                {
                    "currentPoint": '207',
                    "map_x": 22500,
                    "map_y": -21300,
                    "targetPoint": ['206', '208'],
                },
                {
                    "currentPoint": '328',
                    "map_x": 27100,
                    "map_y": -22400,
                    "targetPoint": ['329', '327'],
                },
                {
                    "currentPoint": '329',
                    "map_x": 27100,
                    "map_y": -19000,
                    "targetPoint": ['330', '328'],
                },
                {
                    "currentPoint": '208',
                    "map_x": 22500,
                    "map_y": -22300,
                    "targetPoint": ['207', '209'],
                },
                {
                    "currentPoint": '209',
                    "map_x": 22500,
                    "map_y": -19300,
                    "targetPoint": ['210', '208'],
                },
                {
                    "currentPoint": 'Point-1007',
                    "map_x": 74900,
                    "map_y": -18600,
                    "targetPoint": ['Point-1008', 'Point-0942'],
                },
                {
                    "currentPoint": 'Point-1006',
                    "map_x": 75000,
                    "map_y": -22400,
                    "targetPoint": ['Point-1005', '52'],
                },
                {
                    "currentPoint": 'Point-1005',
                    "map_x": 74900,
                    "map_y": -20900,
                    "targetPoint": ['Point-1006', 'Point-1004'],
                },
                {
                    "currentPoint": 'Point-1004',
                    "map_x": 74900,
                    "map_y": -19600,
                    "targetPoint": ['Point-1005', 'Point-1003'],
                },
                {
                    "currentPoint": 'Point-1009',
                    "map_x": 74900,
                    "map_y": -20900,
                    "targetPoint": ['Point-1010', 'Point-1008'],
                },
                {
                    "currentPoint": 'Point-1008',
                    "map_x": 74900,
                    "map_y": -19600,
                    "targetPoint": ['Point-1009', 'Point-1007'],
                },
                {
                    "currentPoint": '330',
                    "map_x": 27100,
                    "map_y": -20100,
                    "targetPoint": ['331', '329'],
                },
                {
                    "currentPoint": 'Point-1010',
                    "map_x": 75000,
                    "map_y": -22400,
                    "targetPoint": ['53', 'Point-1009'],
                },
                {
                    "currentPoint": '331',
                    "map_x": 27100,
                    "map_y": -21200,
                    "targetPoint": ['332', '330'],
                },
                {
                    "currentPoint": '210',
                    "map_x": 22500,
                    "map_y": -20300,
                    "targetPoint": ['211', '209'],
                },
                {
                    "currentPoint": '211',
                    "map_x": 22500,
                    "map_y": -21300,
                    "targetPoint": ['210', '212'],
                },
                {
                    "currentPoint": '332',
                    "map_x": 27100,
                    "map_y": -22400,
                    "targetPoint": ['37', '331'],
                },
                {
                    "currentPoint": '212',
                    "map_x": 22500,
                    "map_y": -22300,
                    "targetPoint": ['211', '213'],
                },
                {
                    "currentPoint": '213',
                    "map_x": 22500,
                    "map_y": -19300,
                    "targetPoint": ['212', '214'],
                },
                {
                    "currentPoint": '214',
                    "map_x": 22500,
                    "map_y": -20300,
                    "targetPoint": ['213', '215'],
                },
                {
                    "currentPoint": '215',
                    "map_x": 22500,
                    "map_y": -21300,
                    "targetPoint": ['216', '214'],
                },
                {
                    "currentPoint": '216',
                    "map_x": 22500,
                    "map_y": -22300,
                    "targetPoint": ['215', '217'],
                },
                {
                    "currentPoint": '217',
                    "map_x": 22500,
                    "map_y": -19300,
                    "targetPoint": ['218', '216'],
                },
                {
                    "currentPoint": '218',
                    "map_x": 22500,
                    "map_y": -20300,
                    "targetPoint": ['219', '217'],
                },
                {
                    "currentPoint": '219',
                    "map_x": 22500,
                    "map_y": -21300,
                    "targetPoint": ['218', '220'],
                },
                {
                    "currentPoint": '220',
                    "map_x": 22500,
                    "map_y": -22300,
                    "targetPoint": ['219', '221'],
                },
                {
                    "currentPoint": '221',
                    "map_x": 22500,
                    "map_y": -19300,
                    "targetPoint": ['220', '222'],
                },
                {
                    "currentPoint": '100',
                    "map_x": 17800,
                    "map_y": -15700,
                    "targetPoint": ['101'],
                },
                {
                    "currentPoint": '101',
                    "map_x": 17750,
                    "map_y": -19250,
                    "targetPoint": ['102', '100'],
                },
                {
                    "currentPoint": '222',
                    "map_x": 22500,
                    "map_y": -20300,
                    "targetPoint": ['223', '221'],
                },
                {
                    "currentPoint": '223',
                    "map_x": 22500,
                    "map_y": -21300,
                    "targetPoint": ['224', '222'],
                },
                {
                    "currentPoint": '102',
                    "map_x": 17750,
                    "map_y": -20250,
                    "targetPoint": ['101', '103'],
                },
                {
                    "currentPoint": '224',
                    "map_x": 22500,
                    "map_y": -22300,
                    "targetPoint": ['225', '223'],
                },
                {
                    "currentPoint": 'Point-1003',
                    "map_x": 74900,
                    "map_y": -18600,
                    "targetPoint": ['Point-1004', 'Point-0938'],
                },
                {
                    "currentPoint": '103',
                    "map_x": 17750,
                    "map_y": -21250,
                    "targetPoint": ['104', '102'],
                },
                {
                    "currentPoint": '104',
                    "map_x": 17750,
                    "map_y": -22250,
                    "targetPoint": ['103', '105'],
                },
                {
                    "currentPoint": '225',
                    "map_x": 22500,
                    "map_y": -19300,
                    "targetPoint": ['226', '224'],
                },
                {
                    "currentPoint": 'Point-1002',
                    "map_x": 75000,
                    "map_y": -22400,
                    "targetPoint": ['51', 'Point-1001'],
                },
                {
                    "currentPoint": 'Point-1001',
                    "map_x": 74900,
                    "map_y": -20900,
                    "targetPoint": ['Point-1002', 'Point-1000'],
                },
                {
                    "currentPoint": '226',
                    "map_x": 22500,
                    "map_y": -20300,
                    "targetPoint": ['227', '225'],
                },
                {
                    "currentPoint": '105',
                    "map_x": 17750,
                    "map_y": -23750,
                    "targetPoint": ['106', '104'],
                },
                {
                    "currentPoint": '106',
                    "map_x": 17750,
                    "map_y": -24750,
                    "targetPoint": ['107', '105'],
                },
                {
                    "currentPoint": 'Point-1000',
                    "map_x": 74900,
                    "map_y": -19600,
                    "targetPoint": ['Point-0999', 'Point-1001'],
                },
                {
                    "currentPoint": '227',
                    "map_x": 22500,
                    "map_y": -21300,
                    "targetPoint": ['226', '228'],
                },
                {
                    "currentPoint": '107',
                    "map_x": 17750,
                    "map_y": -26000,
                    "targetPoint": ['106', '108'],
                },
                {
                    "currentPoint": '228',
                    "map_x": 22500,
                    "map_y": -22300,
                    "targetPoint": ['227', '229'],
                },
                {
                    "currentPoint": '108',
                    "map_x": 17750,
                    "map_y": -27250,
                    "targetPoint": ['109', '107'],
                },
                {
                    "currentPoint": '229',
                    "map_x": 22500,
                    "map_y": -19300,
                    "targetPoint": ['228', '230'],
                },
                {
                    "currentPoint": '109',
                    "map_x": 17750,
                    "map_y": -29000,
                    "targetPoint": ['110', '108'],
                },
                {
                    "currentPoint": 'Point-0534',
                    "map_x": 75000,
                    "map_y": -22400,
                    "targetPoint": ['Point-0599', 'Point-0533'],
                },
                {
                    "currentPoint": 'Point-0655',
                    "map_x": 74900,
                    "map_y": -18600,
                    "targetPoint": ['Point-0656', 'Point-0590'],
                },
                {
                    "currentPoint": 'Point-0533',
                    "map_x": 74900,
                    "map_y": -20900,
                    "targetPoint": ['Point-0534', 'Point-0532'],
                },
                {
                    "currentPoint": 'Point-0532',
                    "map_x": 74900,
                    "map_y": -19600,
                    "targetPoint": ['Point-0533', 'Point-0531'],
                },
                {
                    "currentPoint": 'Point-0531',
                    "map_x": 74900,
                    "map_y": -18600,
                    "targetPoint": ['Point-0530', 'Point-0532'],
                },
                {
                    "currentPoint": 'Point-0659',
                    "map_x": 74900,
                    "map_y": -18600,
                    "targetPoint": ['Point-0594', 'Point-0660'],
                },
                {
                    "currentPoint": 'Point-0658',
                    "map_x": 75000,
                    "map_y": -22400,
                    "targetPoint": ['Point-0723', 'Point-0657'],
                },
                {
                    "currentPoint": 'Point-0657',
                    "map_x": 74900,
                    "map_y": -20900,
                    "targetPoint": ['Point-0658', 'Point-0656'],
                },
                {
                    "currentPoint": 'Point-0656',
                    "map_x": 74900,
                    "map_y": -19600,
                    "targetPoint": ['Point-0655', 'Point-0657'],
                },
                {
                    "currentPoint": '230',
                    "map_x": 22500,
                    "map_y": -20300,
                    "targetPoint": ['229', '231'],
                },
                {
                    "currentPoint": '110',
                    "map_x": 17750,
                    "map_y": -30000,
                    "targetPoint": ['109', '111'],
                },
                {
                    "currentPoint": '231',
                    "map_x": 22500,
                    "map_y": -21300,
                    "targetPoint": ['232', '230'],
                },
                {
                    "currentPoint": '232',
                    "map_x": 22500,
                    "map_y": -22300,
                    "targetPoint": ['231', '36'],
                },
                {
                    "currentPoint": '111',
                    "map_x": 17750,
                    "map_y": -31250,
                    "targetPoint": ['112', '110'],
                },
                {
                    "currentPoint": '112',
                    "map_x": 17750,
                    "map_y": -32500,
                    "targetPoint": ['111', '113'],
                },
                {
                    "currentPoint": '113',
                    "map_x": 17750,
                    "map_y": -35750,
                    "targetPoint": ['112', '114'],
                },
                {
                    "currentPoint": 'Point-0662',
                    "map_x": 75000,
                    "map_y": -22400,
                    "targetPoint": ['Point-0661', 'Point-0727'],
                },
                {
                    "currentPoint": '114',
                    "map_x": 17750,
                    "map_y": -36750,
                    "targetPoint": ['113', '115'],
                },
                {
                    "currentPoint": 'Point-0661',
                    "map_x": 74900,
                    "map_y": -20900,
                    "targetPoint": ['Point-0660', 'Point-0662'],
                },
                {
                    "currentPoint": '115',
                    "map_x": 17750,
                    "map_y": -37750,
                    "targetPoint": ['114', '116'],
                },
                {
                    "currentPoint": '116',
                    "map_x": 17750,
                    "map_y": -39000,
                    "targetPoint": ['115', '117'],
                },
                {
                    "currentPoint": 'Point-0660',
                    "map_x": 74900,
                    "map_y": -19600,
                    "targetPoint": ['Point-0661', 'Point-0659'],
                },
                {
                    "currentPoint": '117',
                    "map_x": 17750,
                    "map_y": -40250,
                    "targetPoint": ['116', '118'],
                },
                {
                    "currentPoint": '118',
                    "map_x": 17750,
                    "map_y": -41250,
                    "targetPoint": ['119', '117'],
                },
                {
                    "currentPoint": '119',
                    "map_x": 17750,
                    "map_y": -42250,
                    "targetPoint": ['120', '118'],
                },
                {
                    "currentPoint": '120',
                    "map_x": 17750,
                    "map_y": -43500,
                    "targetPoint": ['121', '119'],
                },
                {
                    "currentPoint": '121',
                    "map_x": 17750,
                    "map_y": -45000,
                    "targetPoint": ['120', '122'],
                },
                {
                    "currentPoint": '122',
                    "map_x": 17750,
                    "map_y": -46250,
                    "targetPoint": ['121', '123'],
                },
                {
                    "currentPoint": '123',
                    "map_x": 17750,
                    "map_y": -47250,
                    "targetPoint": ['122', '124'],
                },
                {
                    "currentPoint": '124',
                    "map_x": 17750,
                    "map_y": -48500,
                    "targetPoint": ['125', '123'],
                },
                {
                    "currentPoint": 'Point-0530',
                    "map_x": 70300,
                    "map_y": -15600,
                    "targetPoint": ['Point-0531'],
                },
                {
                    "currentPoint": '125',
                    "map_x": 17750,
                    "map_y": -51500,
                    "targetPoint": ['126', '124'],
                },
                {
                    "currentPoint": '126',
                    "map_x": 17750,
                    "map_y": -52750,
                    "targetPoint": ['127', '125'],
                },
                {
                    "currentPoint": '127',
                    "map_x": 17750,
                    "map_y": -54000,
                    "targetPoint": ['128', '126'],
                },
                {
                    "currentPoint": '128',
                    "map_x": 17750,
                    "map_y": -55250,
                    "targetPoint": ['127', '129'],
                },
                {
                    "currentPoint": '129',
                    "map_x": 17750,
                    "map_y": -56500,
                    "targetPoint": ['130', '128'],
                },
                {
                    "currentPoint": 'Point-0996',
                    "map_x": 74900,
                    "map_y": -19600,
                    "targetPoint": ['Point-0997', 'Point-0995'],
                },
                {
                    "currentPoint": 'Point-0874',
                    "map_x": 75000,
                    "map_y": -22400,
                    "targetPoint": ['Point-0873', 'Point-0939'],
                },
                {
                    "currentPoint": 'Point-0995',
                    "map_x": 74900,
                    "map_y": -18600,
                    "targetPoint": ['Point-0930', 'Point-0996'],
                },
                {
                    "currentPoint": 'Point-0873',
                    "map_x": 74900,
                    "map_y": -20900,
                    "targetPoint": ['Point-0874', 'Point-0872'],
                },
                {
                    "currentPoint": 'Point-0994',
                    "map_x": 75000,
                    "map_y": -22400,
                    "targetPoint": ['49', 'Point-0993'],
                },
                {
                    "currentPoint": 'Point-0993',
                    "map_x": 74900,
                    "map_y": -20900,
                    "targetPoint": ['Point-0992', 'Point-0994'],
                },
                {
                    "currentPoint": 'Point-0872',
                    "map_x": 74900,
                    "map_y": -19600,
                    "targetPoint": ['Point-0871', 'Point-0873'],
                },
                {
                    "currentPoint": 'Point-0999',
                    "map_x": 74900,
                    "map_y": -18600,
                    "targetPoint": ['Point-1000', 'Point-0934'],
                },
                {
                    "currentPoint": 'Point-0998',
                    "map_x": 75000,
                    "map_y": -22400,
                    "targetPoint": ['Point-0997', '50'],
                },
                {
                    "currentPoint": '130',
                    "map_x": 17750,
                    "map_y": -58000,
                    "targetPoint": ['131', '129'],
                },
                {
                    "currentPoint": '131',
                    "map_x": 17750,
                    "map_y": -59000,
                    "targetPoint": ['130', '132'],
                },
                {
                    "currentPoint": 'Point-0997',
                    "map_x": 74900,
                    "map_y": -20900,
                    "targetPoint": ['Point-0996', 'Point-0998'],
                },
                {
                    "currentPoint": '132',
                    "map_x": 17750,
                    "map_y": -60250,
                    "targetPoint": ['35', '131'],
                },
                {
                    "currentPoint": '35',
                    "map_x": 17750,
                    "map_y": -63000,
                    "targetPoint": ['132', '36', '72'],
                },
                {
                    "currentPoint": 'Point-0869',
                    "map_x": 74900,
                    "map_y": -20900,
                    "targetPoint": ['Point-0870', 'Point-0868'],
                },
                {
                    "currentPoint": '36',
                    "map_x": 22500,
                    "map_y": -63000,
                    "targetPoint": ['35', '37', '232'],
                },
                {
                    "currentPoint": '37',
                    "map_x": 27000,
                    "map_y": -63000,
                    "targetPoint": ['36', '38', '332'],
                },
                {
                    "currentPoint": '38',
                    "map_x": 31500,
                    "map_y": -63000,
                    "targetPoint": ['39', '37', '432'],
                },
                {
                    "currentPoint": '39',
                    "map_x": 36500,
                    "map_y": -63000,
                    "targetPoint": ['532', '40', '38'],
                },
                {
                    "currentPoint": 'Point-0864',
                    "map_x": 74900,
                    "map_y": -19600,
                    "targetPoint": ['Point-0865', 'Point-0863'],
                },
                {
                    "currentPoint": 'Point-0501',
                    "map_x": 75000,
                    "map_y": -22400,
                    "targetPoint": ['Point-0500', 'Point-0595'],
                },
                {
                    "currentPoint": 'Point-0500',
                    "map_x": 74900,
                    "map_y": -20900,
                    "targetPoint": ['Point-0499', 'Point-0501'],
                },
                {
                    "currentPoint": 'Point-0863',
                    "map_x": 74900,
                    "map_y": -18600,
                    "targetPoint": ['Point-0864', 'Point-0798'],
                },
                {
                    "currentPoint": 'Point-0862',
                    "map_x": 75000,
                    "map_y": -22400,
                    "targetPoint": ['Point-0927', 'Point-0861'],
                },
                {
                    "currentPoint": 'Point-0861',
                    "map_x": 74900,
                    "map_y": -20900,
                    "targetPoint": ['Point-0862', 'Point-0860'],
                },
                {
                    "currentPoint": 'Point-0868',
                    "map_x": 74900,
                    "map_y": -19600,
                    "targetPoint": ['Point-0867', 'Point-0869'],
                },
                {
                    "currentPoint": 'Point-0867',
                    "map_x": 74900,
                    "map_y": -18600,
                    "targetPoint": ['Point-0802', 'Point-0868'],
                },
                {
                    "currentPoint": 'Point-0866',
                    "map_x": 75000,
                    "map_y": -22400,
                    "targetPoint": ['Point-0865', 'Point-0931'],
                },
                {
                    "currentPoint": 'Point-0865',
                    "map_x": 74900,
                    "map_y": -20900,
                    "targetPoint": ['Point-0866', 'Point-0864'],
                },
                {
                    "currentPoint": 'Point-0871',
                    "map_x": 74900,
                    "map_y": -18600,
                    "targetPoint": ['Point-0806', 'Point-0872'],
                },
                {
                    "currentPoint": 'Point-0992',
                    "map_x": 74900,
                    "map_y": -19600,
                    "targetPoint": ['Point-0991', 'Point-0993'],
                },
                {
                    "currentPoint": 'Point-0870',
                    "map_x": 75000,
                    "map_y": -22400,
                    "targetPoint": ['Point-0869', 'Point-0935'],
                },
                {
                    "currentPoint": 'Point-0991',
                    "map_x": 74900,
                    "map_y": -18600,
                    "targetPoint": ['Point-0926', 'Point-0992'],
                },
                {
                    "currentPoint": '40',
                    "map_x": 41000,
                    "map_y": -63000,
                    "targetPoint": ['632', '39', '41'],
                },
                {
                    "currentPoint": '41',
                    "map_x": 44000,
                    "map_y": -63000,
                    "targetPoint": ['732', '40', '42'],
                },
                {
                    "currentPoint": '42',
                    "map_x": 47000,
                    "map_y": -63000,
                    "targetPoint": ['41', '43', '832'],
                },
                {
                    "currentPoint": '43',
                    "map_x": 52000,
                    "map_y": -63000,
                    "targetPoint": ['932', '42', '44'],
                },
                {
                    "currentPoint": '44',
                    "map_x": 56500,
                    "map_y": -63000,
                    "targetPoint": ['45', '43', '1032'],
                },
                {
                    "currentPoint": '45',
                    "map_x": 60000,
                    "map_y": -63000,
                    "targetPoint": ['46', '44', '1132'],
                },
                {
                    "currentPoint": '46',
                    "map_x": 65000,
                    "map_y": -63000,
                    "targetPoint": ['1232', '48', '45'],
                },
                {
                    "currentPoint": '48',
                    "map_x": 70500,
                    "map_y": -63000,
                    "targetPoint": ['46', '49', '1332'],
                },
                {
                    "currentPoint": '49',
                    "map_x": 75000,
                    "map_y": -63000,
                    "targetPoint": ['50', 'Point-0994', '48'],
                },
                {
                    "currentPoint": 'Point-0464',
                    "map_x": 70300,
                    "map_y": -15600,
                    "targetPoint": ['Point-0465'],
                },
                {
                    "currentPoint": '50',
                    "map_x": 79750,
                    "map_y": -63000,
                    "targetPoint": ['Point-0998', '49', '51'],
                },
                {
                    "currentPoint": '51',
                    "map_x": 84250,
                    "map_y": -63000,
                    "targetPoint": ['Point-1002', '52', '50'],
                },
                {
                    "currentPoint": '52',
                    "map_x": 89000,
                    "map_y": -63000,
                    "targetPoint": ['Point-1006', '53', '51'],
                },
                {
                    "currentPoint": '53',
                    "map_x": 92250,
                    "map_y": -63000,
                    "targetPoint": ['52', 'Point-1010'],
                },
                {
                    "currentPoint": '54',
                    "map_x": 12500,
                    "map_y": -59000,
                    "targetPoint": ['71'],
                },
                {
                    "currentPoint": '56',
                    "map_x": 12500,
                    "map_y": -55000,
                    "targetPoint": ['69'],
                },
                {
                    "currentPoint": '57',
                    "map_x": 12500,
                    "map_y": -53000,
                    "targetPoint": ['68'],
                },
                {
                    "currentPoint": '58',
                    "map_x": 12500,
                    "map_y": -47000,
                    "targetPoint": ['67'],
                },
                {
                    "currentPoint": '59',
                    "map_x": 12500,
                    "map_y": -44500,
                    "targetPoint": ['66'],
                },
                {
                    "currentPoint": '60',
                    "map_x": 12500,
                    "map_y": -43000,
                    "targetPoint": ['65'],
                },
                {
                    "currentPoint": '61',
                    "map_x": 12500,
                    "map_y": -41000,
                    "targetPoint": ['64'],
                },
                {
                    "currentPoint": '62',
                    "map_x": 12500,
                    "map_y": -39000,
                    "targetPoint": ['63'],
                },
                {
                    "currentPoint": '63',
                    "map_x": 9250,
                    "map_y": -39000,
                    "targetPoint": ['62', '64'],
                },
                {
                    "currentPoint": '64',
                    "map_x": 9250,
                    "map_y": -41000,
                    "targetPoint": ['65', '61', '63'],
                },
                {
                    "currentPoint": '65',
                    "map_x": 9250,
                    "map_y": -43000,
                    "targetPoint": ['60', '66', '64'],
                },
                {
                    "currentPoint": '66',
                    "map_x": 9250,
                    "map_y": -44500,
                    "targetPoint": ['59', '67', '65'],
                },
                {
                    "currentPoint": '67',
                    "map_x": 9250,
                    "map_y": -47000,
                    "targetPoint": ['66', '68', '58'],
                },
                {
                    "currentPoint": '68',
                    "map_x": 9250,
                    "map_y": -53000,
                    "targetPoint": ['67', '69', '57'],
                },
                {
                    "currentPoint": '69',
                    "map_x": 9250,
                    "map_y": -55000,
                    "targetPoint": ['68', '56', '70'],
                },
                {
                    "currentPoint": 'Point-0798',
                    "map_x": 75000,
                    "map_y": -22400,
                    "targetPoint": ['Point-0863', 'Point-0797'],
                },
                {
                    "currentPoint": 'Point-0435',
                    "map_x": 75000,
                    "map_y": -22400,
                    "targetPoint": ['Point-0587', 'Point-0434'],
                },
                {
                    "currentPoint": 'Point-0434',
                    "map_x": 74900,
                    "map_y": -20900,
                    "targetPoint": ['Point-0435', 'Point-0433'],
                },
                {
                    "currentPoint": 'Point-0797',
                    "map_x": 74900,
                    "map_y": -20900,
                    "targetPoint": ['Point-0798', 'Point-0796'],
                },
                {
                    "currentPoint": 'Point-0433',
                    "map_x": 74900,
                    "map_y": -19600,
                    "targetPoint": ['Point-0434', 'Point-0432'],
                },
                {
                    "currentPoint": 'Point-0796',
                    "map_x": 74900,
                    "map_y": -19600,
                    "targetPoint": ['Point-0795', 'Point-0797'],
                },
                {
                    "currentPoint": 'Point-0432',
                    "map_x": 74900,
                    "map_y": -18600,
                    "targetPoint": ['Point-0431', 'Point-0433'],
                },
                {
                    "currentPoint": 'Point-0795',
                    "map_x": 74900,
                    "map_y": -18600,
                    "targetPoint": ['Point-0796', 'Point-0730'],
                },
                {
                    "currentPoint": 'Point-0799',
                    "map_x": 74900,
                    "map_y": -18600,
                    "targetPoint": ['Point-0734', 'Point-0800'],
                },
                {
                    "currentPoint": '70',
                    "map_x": 9250,
                    "map_y": -57000,
                    "targetPoint": ['55', '69', '71'],
                },
                {
                    "currentPoint": '71',
                    "map_x": 9250,
                    "map_y": -59000,
                    "targetPoint": ['72', '70', '54'],
                },
                {
                    "currentPoint": '72',
                    "map_x": 9250,
                    "map_y": -63000,
                    "targetPoint": ['35', '71'],
                },
                {
                    "currentPoint": 'Point-0666',
                    "map_x": 75000,
                    "map_y": -22400,
                    "targetPoint": ['Point-0731', 'Point-0665'],
                },
                {
                    "currentPoint": 'Point-0665',
                    "map_x": 74900,
                    "map_y": -20900,
                    "targetPoint": ['Point-0664', 'Point-0666'],
                },
                {
                    "currentPoint": 'Point-0664',
                    "map_x": 74900,
                    "map_y": -19600,
                    "targetPoint": ['Point-0663', 'Point-0665'],
                },
                {
                    "currentPoint": 'Point-0663',
                    "map_x": 74900,
                    "map_y": -18600,
                    "targetPoint": ['Point-0598', 'Point-0664'],
                },
                {
                    "currentPoint": 'Point-0669',
                    "map_x": 74900,
                    "map_y": -20900,
                    "targetPoint": ['Point-0668', 'Point-0670'],
                },
                {
                    "currentPoint": 'Point-0668',
                    "map_x": 74900,
                    "map_y": -19600,
                    "targetPoint": ['Point-0669', 'Point-0667'],
                },
                {
                    "currentPoint": 'Point-0667',
                    "map_x": 74900,
                    "map_y": -18600,
                    "targetPoint": ['Point-0668', 'Point-0602'],
                },
                {
                    "currentPoint": 'Point-0431',
                    "map_x": 70300,
                    "map_y": -15600,
                    "targetPoint": ['Point-0432'],
                },
                {
                    "currentPoint": 'Point-0794',
                    "map_x": 75000,
                    "map_y": -22400,
                    "targetPoint": ['Point-0859', 'Point-0793'],
                },
                {
                    "currentPoint": 'Point-0793',
                    "map_x": 74900,
                    "map_y": -20900,
                    "targetPoint": ['Point-0794', 'Point-0792'],
                },
                {
                    "currentPoint": 'Point-0792',
                    "map_x": 74900,
                    "map_y": -19600,
                    "targetPoint": ['Point-0793', 'Point-0791'],
                },
                {
                    "currentPoint": 'Point-0670',
                    "map_x": 75000,
                    "map_y": -22400,
                    "targetPoint": ['Point-0735', 'Point-0669'],
                },
                {
                    "currentPoint": 'Point-0791',
                    "map_x": 74900,
                    "map_y": -18600,
                    "targetPoint": ['Point-0792', 'Point-0726'],
                },
                {
                    "currentPoint": 'Point-0938',
                    "map_x": 75000,
                    "map_y": -22400,
                    "targetPoint": ['Point-0937', 'Point-1003'],
                },
                {
                    "currentPoint": 'Point-0937',
                    "map_x": 74900,
                    "map_y": -20900,
                    "targetPoint": ['Point-0938', 'Point-0936'],
                },
                {
                    "currentPoint": 'Point-0936',
                    "map_x": 74900,
                    "map_y": -19600,
                    "targetPoint": ['Point-0937', 'Point-0935'],
                },
                {
                    "currentPoint": 'Point-0935',
                    "map_x": 74900,
                    "map_y": -18600,
                    "targetPoint": ['Point-0936', 'Point-0870'],
                },
                {
                    "currentPoint": 'Point-0939',
                    "map_x": 74900,
                    "map_y": -18600,
                    "targetPoint": ['Point-0874', 'Point-0940'],
                },
                {
                    "currentPoint": 'Point-0930',
                    "map_x": 75000,
                    "map_y": -22400,
                    "targetPoint": ['Point-0995', 'Point-0929'],
                },
                {
                    "currentPoint": 'Point-0934',
                    "map_x": 75000,
                    "map_y": -22400,
                    "targetPoint": ['Point-0933', 'Point-0999'],
                },
                {
                    "currentPoint": 'Point-0933',
                    "map_x": 74900,
                    "map_y": -20900,
                    "targetPoint": ['Point-0934', 'Point-0932'],
                },
                {
                    "currentPoint": 'Point-0932',
                    "map_x": 74900,
                    "map_y": -19600,
                    "targetPoint": ['Point-0933', 'Point-0931'],
                },
                {
                    "currentPoint": 'Point-0931',
                    "map_x": 74900,
                    "map_y": -18600,
                    "targetPoint": ['Point-0932', 'Point-0866'],
                },
                {
                    "currentPoint": 'Point-0927',
                    "map_x": 74900,
                    "map_y": -18600,
                    "targetPoint": ['Point-0928', 'Point-0862'],
                },
                {
                    "currentPoint": 'Point-0806',
                    "map_x": 75000,
                    "map_y": -22400,
                    "targetPoint": ['Point-0871', 'Point-0805'],
                },
                {
                    "currentPoint": 'Point-0805',
                    "map_x": 74900,
                    "map_y": -20900,
                    "targetPoint": ['Point-0804', 'Point-0806'],
                },
                {
                    "currentPoint": 'Point-0926',
                    "map_x": 75000,
                    "map_y": -22400,
                    "targetPoint": ['Point-0991', 'Point-0925'],
                },
                {
                    "currentPoint": 'Point-0804',
                    "map_x": 74900,
                    "map_y": -19600,
                    "targetPoint": ['Point-0803', 'Point-0805'],
                },
                {
                    "currentPoint": 'Point-0925',
                    "map_x": 74900,
                    "map_y": -20900,
                    "targetPoint": ['Point-0924', 'Point-0926'],
                },
                {
                    "currentPoint": 'Point-0924',
                    "map_x": 74900,
                    "map_y": -19600,
                    "targetPoint": ['Point-0925', 'Point-0923'],
                },
                {
                    "currentPoint": 'Point-0803',
                    "map_x": 74900,
                    "map_y": -18600,
                    "targetPoint": ['Point-0804', 'Point-0738'],
                },
                {
                    "currentPoint": 'Point-0929',
                    "map_x": 74900,
                    "map_y": -20900,
                    "targetPoint": ['Point-0930', 'Point-0928'],
                },
                {
                    "currentPoint": 'Point-0928',
                    "map_x": 74900,
                    "map_y": -19600,
                    "targetPoint": ['Point-0929', 'Point-0927'],
                },
                {
                    "currentPoint": 'Point-0802',
                    "map_x": 75000,
                    "map_y": -22400,
                    "targetPoint": ['Point-0867', 'Point-0801'],
                },
                {
                    "currentPoint": 'Point-0923',
                    "map_x": 74900,
                    "map_y": -18600,
                    "targetPoint": ['1424', 'Point-0924'],
                },
                {
                    "currentPoint": 'Point-0801',
                    "map_x": 74900,
                    "map_y": -20900,
                    "targetPoint": ['Point-0800', 'Point-0802'],
                },
                {
                    "currentPoint": 'Point-0800',
                    "map_x": 74900,
                    "map_y": -19600,
                    "targetPoint": ['Point-0799', 'Point-0801'],
                },
                {
                    "currentPoint": '1403',
                    "map_x": 75000,
                    "map_y": -22400,
                    "targetPoint": ['1405', '1402', '1403'],
                },
                {
                    "currentPoint": '1402',
                    "map_x": 74900,
                    "map_y": -19600,
                    "targetPoint": ['1401', '1403'],
                },
                {
                    "currentPoint": '1401',
                    "map_x": 74900,
                    "map_y": -18600,
                    "targetPoint": ['1400', '1402'],
                },
                {
                    "currentPoint": '1400',
                    "map_x": 70300,
                    "map_y": -15600,
                    "targetPoint": ['1401'],
                },
                {
                    "currentPoint": '1409',
                    "map_x": 74900,
                    "map_y": -18600,
                    "targetPoint": ['1410', '1408'],
                },
                {
                    "currentPoint": '1408',
                    "map_x": 75000,
                    "map_y": -22400,
                    "targetPoint": ['1407', '1409'],
                },
                {
                    "currentPoint": '1407',
                    "map_x": 74900,
                    "map_y": -20900,
                    "targetPoint": ['1406', '1408'],
                },
                {
                    "currentPoint": '1406',
                    "map_x": 74900,
                    "map_y": -19600,
                    "targetPoint": ['1405', '1407'],
                },
                {
                    "currentPoint": '1405',
                    "map_x": 74900,
                    "map_y": -18600,
                    "targetPoint": ['1406', '1403'],
                },
                {
                    "currentPoint": 'Point-0738',
                    "map_x": 75000,
                    "map_y": -22400,
                    "targetPoint": ['Point-0737', 'Point-0803'],
                },
                {
                    "currentPoint": 'Point-0859',
                    "map_x": 74900,
                    "map_y": -18600,
                    "targetPoint": ['Point-0860', 'Point-0794'],
                },
                {
                    "currentPoint": 'Point-0737',
                    "map_x": 74900,
                    "map_y": -20900,
                    "targetPoint": ['Point-0736', 'Point-0738'],
                },
                {
                    "currentPoint": 'Point-0732',
                    "map_x": 74900,
                    "map_y": -19600,
                    "targetPoint": ['Point-0731', 'Point-0733'],
                },
                {
                    "currentPoint": 'Point-0731',
                    "map_x": 74900,
                    "map_y": -18600,
                    "targetPoint": ['Point-0666', 'Point-0732'],
                },
                {
                    "currentPoint": 'Point-0730',
                    "map_x": 75000,
                    "map_y": -22400,
                    "targetPoint": ['Point-0795', 'Point-0729'],
                },
                {
                    "currentPoint": 'Point-0736',
                    "map_x": 74900,
                    "map_y": -19600,
                    "targetPoint": ['Point-0735', 'Point-0737'],
                },
                {
                    "currentPoint": 'Point-0735',
                    "map_x": 74900,
                    "map_y": -18600,
                    "targetPoint": ['Point-0736', 'Point-0670'],
                },
                {
                    "currentPoint": 'Point-0734',
                    "map_x": 75000,
                    "map_y": -22400,
                    "targetPoint": ['Point-0799', 'Point-0733'],
                },
                {
                    "currentPoint": 'Point-0733',
                    "map_x": 74900,
                    "map_y": -20900,
                    "targetPoint": ['Point-0732', 'Point-0734'],
                },
                {
                    "currentPoint": '1415',
                    "map_x": 74900,
                    "map_y": -20900,
                    "targetPoint": ['1414', '1416'],
                },
                {
                    "currentPoint": '1414',
                    "map_x": 74900,
                    "map_y": -19600,
                    "targetPoint": ['1413', '1415'],
                },
                {
                    "currentPoint": '1413',
                    "map_x": 74900,
                    "map_y": -18600,
                    "targetPoint": ['1412', '1414'],
                },
                {
                    "currentPoint": '1412',
                    "map_x": 75000,
                    "map_y": -22400,
                    "targetPoint": ['1413', '1411'],
                },
                {
                    "currentPoint": 'Point-0860',
                    "map_x": 74900,
                    "map_y": -19600,
                    "targetPoint": ['Point-0859', 'Point-0861'],
                },
                {
                    "currentPoint": '1411',
                    "map_x": 74900,
                    "map_y": -20900,
                    "targetPoint": ['1412', '1410'],
                },
                {
                    "currentPoint": '1410',
                    "map_x": 74900,
                    "map_y": -19600,
                    "targetPoint": ['1409', '1411'],
                },
                {
                    "currentPoint": '1419',
                    "map_x": 74900,
                    "map_y": -20900,
                    "targetPoint": ['1418', '1420'],
                },
                {
                    "currentPoint": '1418',
                    "map_x": 74900,
                    "map_y": -19600,
                    "targetPoint": ['1417', '1419'],
                },
                {
                    "currentPoint": '1417',
                    "map_x": 74900,
                    "map_y": -18600,
                    "targetPoint": ['1418', '1416'],
                },
                {
                    "currentPoint": '1416',
                    "map_x": 75000,
                    "map_y": -22400,
                    "targetPoint": ['1417', '1415'],
                },
                {
                    "currentPoint": 'Point-0729',
                    "map_x": 74900,
                    "map_y": -20900,
                    "targetPoint": ['Point-0730', 'Point-0728'],
                },
                {
                    "currentPoint": 'Point-0728',
                    "map_x": 74900,
                    "map_y": -19600,
                    "targetPoint": ['Point-0727', 'Point-0729'],
                },
                {
                    "currentPoint": 'Point-0727',
                    "map_x": 74900,
                    "map_y": -18600,
                    "targetPoint": ['Point-0662', 'Point-0728'],
                },
                {
                    "currentPoint": 'Point-0726',
                    "map_x": 75000,
                    "map_y": -22400,
                    "targetPoint": ['Point-0725', 'Point-0791'],
                },
                {
                    "currentPoint": 'Point-0600',
                    "map_x": 74900,
                    "map_y": -19600,
                    "targetPoint": ['Point-0601', 'Point-0599'],
                },
                {
                    "currentPoint": 'Point-0725',
                    "map_x": 74900,
                    "map_y": -20900,
                    "targetPoint": ['Point-0726', 'Point-0724'],
                },
                {
                    "currentPoint": 'Point-0724',
                    "map_x": 74900,
                    "map_y": -19600,
                    "targetPoint": ['Point-0723', 'Point-0725'],
                },
                {
                    "currentPoint": 'Point-0723',
                    "map_x": 74900,
                    "map_y": -18600,
                    "targetPoint": ['Point-0658', 'Point-0724'],
                },
                {
                    "currentPoint": 'Point-0602',
                    "map_x": 75000,
                    "map_y": -22400,
                    "targetPoint": ['Point-0601', 'Point-0667'],
                },
                {
                    "currentPoint": 'Point-0601',
                    "map_x": 74900,
                    "map_y": -20900,
                    "targetPoint": ['Point-0602', 'Point-0600'],
                },
                {
                    "currentPoint": '1305',
                    "map_x": 70300,
                    "map_y": -18600,
                    "targetPoint": ['1306', '1304'],
                },
                {
                    "currentPoint": '1304',
                    "map_x": 70300,
                    "map_y": -22400,
                    "targetPoint": ['1303', '1305'],
                },
                {
                    "currentPoint": '1424',
                    "map_x": 75000,
                    "map_y": -22400,
                    "targetPoint": ['Point-0923', '1423'],
                },
                {
                    "currentPoint": '1303',
                    "map_x": 70300,
                    "map_y": -21000,
                    "targetPoint": ['1302', '1304'],
                },
                {
                    "currentPoint": '1423',
                    "map_x": 74900,
                    "map_y": -20900,
                    "targetPoint": ['1424', '1422'],
                },
                {
                    "currentPoint": '1302',
                    "map_x": 70300,
                    "map_y": -19700,
                    "targetPoint": ['1301', '1303'],
                },
                {
                    "currentPoint": '1301',
                    "map_x": 70300,
                    "map_y": -18600,
                    "targetPoint": ['1302', '1300'],
                },
                {
                    "currentPoint": '1422',
                    "map_x": 74900,
                    "map_y": -19600,
                    "targetPoint": ['1423', '1421'],
                },
                {
                    "currentPoint": '1300',
                    "map_x": 70300,
                    "map_y": -15600,
                    "targetPoint": ['1301'],
                },
                {
                    "currentPoint": '1421',
                    "map_x": 74900,
                    "map_y": -18600,
                    "targetPoint": ['1420', '1422'],
                },
                {
                    "currentPoint": '1420',
                    "map_x": 75000,
                    "map_y": -22400,
                    "targetPoint": ['1419', '1421'],
                },
                {
                    "currentPoint": '1309',
                    "map_x": 70300,
                    "map_y": -18600,
                    "targetPoint": ['1310', '1308'],
                },
                {
                    "currentPoint": '1308',
                    "map_x": 70300,
                    "map_y": -22400,
                    "targetPoint": ['1307', '1309'],
                },
                {
                    "currentPoint": '1307',
                    "map_x": 70300,
                    "map_y": -21000,
                    "targetPoint": ['1306', '1308'],
                },
                {
                    "currentPoint": '1306',
                    "map_x": 70300,
                    "map_y": -19700,
                    "targetPoint": ['1307', '1305'],
                },
                {
                    "currentPoint": '1316',
                    "map_x": 70300,
                    "map_y": -22400,
                    "targetPoint": ['1315', '1317'],
                },
                {
                    "currentPoint": '1315',
                    "map_x": 70300,
                    "map_y": -21000,
                    "targetPoint": ['1314', '1316'],
                },
                {
                    "currentPoint": '1314',
                    "map_x": 70300,
                    "map_y": -19700,
                    "targetPoint": ['1313', '1315'],
                },
                {
                    "currentPoint": '1313',
                    "map_x": 70300,
                    "map_y": -18600,
                    "targetPoint": ['1314', '1312'],
                },
                {
                    "currentPoint": '1312',
                    "map_x": 70300,
                    "map_y": -22400,
                    "targetPoint": ['1313', '1311'],
                },
                {
                    "currentPoint": '1311',
                    "map_x": 70300,
                    "map_y": -21000,
                    "targetPoint": ['1312', '1310'],
                },
                {
                    "currentPoint": '1310',
                    "map_x": 70300,
                    "map_y": -19700,
                    "targetPoint": ['1309', '1311'],
                },
                {
                    "currentPoint": '1319',
                    "map_x": 70300,
                    "map_y": -21000,
                    "targetPoint": ['1318', '1320'],
                },
                {
                    "currentPoint": '1318',
                    "map_x": 70300,
                    "map_y": -19700,
                    "targetPoint": ['1319', '1317'],
                },
                {
                    "currentPoint": '1317',
                    "map_x": 70300,
                    "map_y": -18600,
                    "targetPoint": ['1318', '1316'],
                },
                {
                    "currentPoint": '1330',
                    "map_x": 70300,
                    "map_y": -19700,
                    "targetPoint": ['1329', '1331'],
                },
                {
                    "currentPoint": 'Point-0941',
                    "map_x": 74900,
                    "map_y": -20900,
                    "targetPoint": ['Point-0942', 'Point-0940'],
                },
                {
                    "currentPoint": 'Point-0940',
                    "map_x": 74900,
                    "map_y": -19600,
                    "targetPoint": ['Point-0941', 'Point-0939'],
                },
                {
                    "currentPoint": 'Point-0942',
                    "map_x": 75000,
                    "map_y": -22400,
                    "targetPoint": ['Point-0941', 'Point-1007'],
                },
                {
                    "currentPoint": '1206',
                    "map_x": 64700,
                    "map_y": -20100,
                    "targetPoint": ['1207', '1205'],
                },
                {
                    "currentPoint": '1327',
                    "map_x": 70300,
                    "map_y": -21000,
                    "targetPoint": ['1326', '1328'],
                },
                {
                    "currentPoint": '1326',
                    "map_x": 70300,
                    "map_y": -19700,
                    "targetPoint": ['1325', '1327'],
                },
                {
                    "currentPoint": '1205',
                    "map_x": 64700,
                    "map_y": -18700,
                    "targetPoint": ['1204', '1206'],
                },
                {
                    "currentPoint": '1325',
                    "map_x": 70300,
                    "map_y": -18600,
                    "targetPoint": ['1326', '1324'],
                },
                {
                    "currentPoint": '1204',
                    "map_x": 64800,
                    "map_y": -22500,
                    "targetPoint": ['1203', '1205'],
                },
                {
                    "currentPoint": '1324',
                    "map_x": 70300,
                    "map_y": -22400,
                    "targetPoint": ['1325', '1323'],
                },
                {
                    "currentPoint": '1203',
                    "map_x": 64800,
                    "map_y": -21200,
                    "targetPoint": ['1202', '1204'],
                },
                {
                    "currentPoint": '1202',
                    "map_x": 64700,
                    "map_y": -20100,
                    "targetPoint": ['1203', '1201'],
                },
                {
                    "currentPoint": '1323',
                    "map_x": 70300,
                    "map_y": -21000,
                    "targetPoint": ['1322', '1324'],
                },
                {
                    "currentPoint": '1201',
                    "map_x": 64700,
                    "map_y": -18700,
                    "targetPoint": ['1202', '1200'],
                },
                {
                    "currentPoint": '1322',
                    "map_x": 70300,
                    "map_y": -19700,
                    "targetPoint": ['1321', '1323'],
                },
                {
                    "currentPoint": '1321',
                    "map_x": 70300,
                    "map_y": -18600,
                    "targetPoint": ['1320', '1322'],
                },
                {
                    "currentPoint": '1200',
                    "map_x": 64700,
                    "map_y": -15500,
                    "targetPoint": ['1201'],
                },
                {
                    "currentPoint": '1320',
                    "map_x": 70300,
                    "map_y": -22400,
                    "targetPoint": ['1319', '1321'],
                },
                {
                    "currentPoint": '900',
                    "map_x": 51800,
                    "map_y": -15600,
                    "targetPoint": ['901'],
                },
                {
                    "currentPoint": '901',
                    "map_x": 51800,
                    "map_y": -18800,
                    "targetPoint": ['902', '900'],
                },
                {
                    "currentPoint": '902',
                    "map_x": 51700,
                    "map_y": -20000,
                    "targetPoint": ['901', '903'],
                },
                {
                    "currentPoint": '903',
                    "map_x": 51700,
                    "map_y": -21200,
                    "targetPoint": ['902', '904'],
                },
                {
                    "currentPoint": '1209',
                    "map_x": 64700,
                    "map_y": -18700,
                    "targetPoint": ['1208', '1210'],
                },
                {
                    "currentPoint": '904',
                    "map_x": 51700,
                    "map_y": -22600,
                    "targetPoint": ['905', '903'],
                },
                {
                    "currentPoint": '1208',
                    "map_x": 64800,
                    "map_y": -22500,
                    "targetPoint": ['1207', '1209'],
                },
                {
                    "currentPoint": '905',
                    "map_x": 51800,
                    "map_y": -18800,
                    "targetPoint": ['904', '906'],
                },
                {
                    "currentPoint": '1329',
                    "map_x": 70300,
                    "map_y": -18600,
                    "targetPoint": ['1328', '1330'],
                },
                {
                    "currentPoint": '1328',
                    "map_x": 70300,
                    "map_y": -22400,
                    "targetPoint": ['1327', '1329'],
                },
                {
                    "currentPoint": '906',
                    "map_x": 51700,
                    "map_y": -20000,
                    "targetPoint": ['905', '907'],
                },
                {
                    "currentPoint": '1207',
                    "map_x": 64800,
                    "map_y": -21200,
                    "targetPoint": ['1208', '1206'],
                },
            ]
        },
        "meta": {
            "msg": "地图信息成功", "status": 200
        }
    }
    return ret


@app.route('/getAgvState', methods=['GET', 'POST'])
def getAgvState():
    args = request.get_data()
    print(args)
    ret = {
        "data": {
            "total": 1,
            "pagenum": 0,
            "agvList": [
                {
                "agvArea": "null",
                "agvId": 'agv031',
                "taskId": 'Task_20210619101513075',
                "taskIndex": 1,
                "moveStatus": 'stop',
                "agvStopReasonS": "STOP_CARD",
                "batteryLevel": 80,
                "headingAngle": '-90',
                "ipAddress": '127.0.0.1:47340',
                "loading": [0, 0, 1, 1, 0, 1],
                "onLine": 'on',
                "powerChargeLevelHigh": 0,
                "powerChargeLevelLow": 0,
                "powerChargeLevelOff": 0,
                "now": '11908',
                "to": "10205",
                "yet": "10203",
                "speed": 1.0,
                "taskCount": 5,
                "taskEndTime": "null",
                "taskList": [
                    '10203',
                    '10204',
                    '10205',
                    '10206',
                    '10207',
                ],
                "taskStatus": 'task',
                "unBlock": '1',
                "updateTime": '2021-06-19 10:53:20',
                "taskActionLists":[],
                "taskActionList":[
                    {
                        "pointId": 1000000016,
                        "action": "1_(_GR21E_000000_ffffff)",
                        "finishTime": "2021-09-08 15:00:00 / 进行中"
                    },
                    {
                        "pointId": 1000000016,
                        "action": "2_(_PL53R_000000_567456,_PL54R_000000_ffffff)",
                        "finishTime": "2021-09-08 15:00:00 / 进行中"
                    },
                    {
                        "pointId": 1000000016,
                        "action": "1_(_PR21E_000000_ffffff)",
                        "finishTime": "2021-09-08 15:00:00 / 进行中"
                    },
                    {
                        "pointId": 1000000016,
                        "action": "2_(_GL53R_000000_ffffff,_PL54R_000000_ffffff)",
                        "finishTime": ""
                    },
                    {
                        "pointId": 1000000016,
                        "action": "1_(_GR21E_000000_ffffff)",
                        "finishTime": "2021-09-08 15:00:00 / 进行中"
                    },
                    {
                        "pointId": 1000000016,
                        "action": "1_(_GR21E_000000_ffffff)",
                        "finishTime": "2021-09-08 15:00:00 / 进行中"
                    },
                    {
                        "pointId": 1000000016,
                        "action": "1_(_GR21E_000000_ffffff)",
                        "finishTime": "2021-09-08 15:00:00 / 进行中"
                    }
                ],
                "taskActionIndex": 2,
            },
                {
                "agvArea": "null",
                "agvId": 'agv011',
                "taskId": 'Task_20210619101513075',
                "taskIndex": 1,
                "moveStatus": 'stop',
                "agvStopReasonS": "STOP_CARD",
                "batteryLevel": 80,
                "headingAngle": '-90',
                "ipAddress": '127.0.0.1:47340',
                "loading": [0, 0, 1, 1, 0, 1],
                "onLine": 'on',
                "powerChargeLevelHigh": 0,
                "powerChargeLevelLow": 0,
                "powerChargeLevelOff": 0,
                "now": '10225',
                "to": "10205",
                "yet": "10203",
                "speed": 1.0,
                "taskCount": 5,
                "taskEndTime": "null",
                "taskList": [
                    '10203',
                    '10204',
                    '10205',
                    '10206',
                    '10207',
                ],
                "taskStatus": 'task',
                "unBlock": '1',
                "updateTime": '2021-06-19 10:53:20',
                "taskActionLists":[],
                "taskActionList":[
                    {
                        "pointId": 1000000016,
                        "action": "1_(_GR21E_000000_ffffff)",
                        "finishTime": "2021-09-08 15:00:00 / 进行中"
                    },
                    {
                        "pointId": 1000000016,
                        "action": "2_(_PL53R_000000_567456,_PL54R_000000_ffffff)",
                        "finishTime": "2021-09-08 15:00:00 / 进行中"
                    },
                    {
                        "pointId": 1000000016,
                        "action": "1_(_PR21E_000000_ffffff)",
                        "finishTime": "2021-09-08 15:00:00 / 进行中"
                    },
                    {
                        "pointId": 1000000016,
                        "action": "2_(_GL53R_000000_ffffff,_PL54R_000000_ffffff)",
                        "finishTime": ""
                    },
                    {
                        "pointId": 1000000016,
                        "action": "1_(_GR21E_000000_ffffff)",
                        "finishTime": "2021-09-08 15:00:00 / 进行中"
                    },
                    {
                        "pointId": 1000000016,
                        "action": "1_(_GR21E_000000_ffffff)",
                        "finishTime": "2021-09-08 15:00:00 / 进行中"
                    },
                    {
                        "pointId": 1000000016,
                        "action": "1_(_GR21E_000000_ffffff)",
                        "finishTime": "2021-09-08 15:00:00 / 进行中"
                    }
                ],
                "taskActionIndex": 2,
            },
                {
                "agvArea": "null",
                "agvId": 'agv021',
                "taskId": 'Task_20210619101513075',
                "taskIndex": 1,
                "moveStatus": 'stop',
                "agvStopReasonS": "STOP_CARD",
                "batteryLevel": 80,
                "headingAngle": '-90',
                "ipAddress": '127.0.0.1:47340',
                "loading": [0, 0, 1, 1, 0, 1],
                "onLine": 'on',
                "powerChargeLevelHigh": 0,
                "powerChargeLevelLow": 0,
                "powerChargeLevelOff": 0,
                "now": '11802',
                "to": "10205",
                "yet": "10203",
                "speed": 1.0,
                "taskCount": 5,
                "taskEndTime": "null",
                "taskList": [
                    '10203',
                    '10204',
                    '10205',
                    '10206',
                    '10207',
                ],
                "taskStatus": 'task',
                "unBlock": '1',
                "updateTime": '2021-06-19 10:53:20',
                "taskActionLists":[],
                "taskActionList":[
                    {
                        "pointId": 1000000016,
                        "action": "1_(_GR21E_000000_ffffff)",
                        "finishTime": "2021-09-08 15:00:00 / 进行中"
                    },
                    {
                        "pointId": 1000000016,
                        "action": "2_(_PL53R_000000_567456,_PL54R_000000_ffffff)",
                        "finishTime": "2021-09-08 15:00:00 / 进行中"
                    },
                    {
                        "pointId": 1000000016,
                        "action": "1_(_PR21E_000000_ffffff)",
                        "finishTime": "2021-09-08 15:00:00 / 进行中"
                    },
                    {
                        "pointId": 1000000016,
                        "action": "2_(_GL53R_000000_ffffff,_PL54R_000000_ffffff)",
                        "finishTime": ""
                    },
                    {
                        "pointId": 1000000016,
                        "action": "1_(_GR21E_000000_ffffff)",
                        "finishTime": "2021-09-08 15:00:00 / 进行中"
                    },
                    {
                        "pointId": 1000000016,
                        "action": "1_(_GR21E_000000_ffffff)",
                        "finishTime": "2021-09-08 15:00:00 / 进行中"
                    },
                    {
                        "pointId": 1000000016,
                        "action": "1_(_GR21E_000000_ffffff)",
                        "finishTime": "2021-09-08 15:00:00 / 进行中"
                    }
                ],
                "taskActionIndex": 2,
            },
                {
                "agvArea": "null",
                "agvId": 'agv022',
                "taskId": 'Task_20210619101513075',
                "taskIndex": 1,
                "moveStatus": 'stop',
                "agvStopReasonS": "STOP_CARD",
                "batteryLevel": 80,
                "headingAngle": '-90',
                "ipAddress": '127.0.0.1:47340',
                "loading": [0, 0, 1, 1, 0, 1],
                "onLine": 'on',
                "powerChargeLevelHigh": 0,
                "powerChargeLevelLow": 0,
                "powerChargeLevelOff": 0,
                "now": '11902',
                "to": "10205",
                "yet": "10203",
                "speed": 1.0,
                "taskCount": 5,
                "taskEndTime": "null",
                "taskList": [
                    '10203',
                    '10204',
                    '10205',
                    '10206',
                    '10207',
                ],
                "taskStatus": 'task',
                "unBlock": '1',
                "updateTime": '2021-06-19 10:53:20',
                "taskActionLists":[],
                "taskActionList":[
                    {
                        "pointId": 1000000016,
                        "action": "1_(_GR21E_000000_ffffff)",
                        "finishTime": "2021-09-08 15:00:00 / 进行中"
                    },
                    {
                        "pointId": 1000000016,
                        "action": "2_(_PL53R_000000_567456,_PL54R_000000_ffffff)",
                        "finishTime": "2021-09-08 15:00:00 / 进行中"
                    },
                    {
                        "pointId": 1000000016,
                        "action": "1_(_PR21E_000000_ffffff)",
                        "finishTime": "2021-09-08 15:00:00 / 进行中"
                    },
                    {
                        "pointId": 1000000016,
                        "action": "2_(_GL53R_000000_ffffff,_PL54R_000000_ffffff)",
                        "finishTime": ""
                    },
                    {
                        "pointId": 1000000016,
                        "action": "1_(_GR21E_000000_ffffff)",
                        "finishTime": "2021-09-08 15:00:00 / 进行中"
                    },
                    {
                        "pointId": 1000000016,
                        "action": "1_(_GR21E_000000_ffffff)",
                        "finishTime": "2021-09-08 15:00:00 / 进行中"
                    },
                    {
                        "pointId": 1000000016,
                        "action": "1_(_GR21E_000000_ffffff)",
                        "finishTime": "2021-09-08 15:00:00 / 进行中"
                    }
                ],
                "taskActionIndex": 2,
            },
                {
                "agvArea": "null",
                "agvId": 'agv006',
                "taskId": 'Task_20210619101513075',
                "taskIndex": 1,
                "moveStatus": 'stop',
                "agvStopReasonS": "STOP_CARD",
                "batteryLevel": 80,
                "headingAngle": '-90',
                "ipAddress": '127.0.0.1:47340',
                "loading": [0, 0, 1, 1, 0, 1],
                "onLine": 'on',
                "powerChargeLevelHigh": 0,
                "powerChargeLevelLow": 0,
                "powerChargeLevelOff": 0,
                "now": '10201',
                "to": "10205",
                "yet": "10203",
                "speed": 1.0,
                "taskCount": 5,
                "taskEndTime": "null",
                "taskList": [
                    '10203',
                    '10204',
                    '10205',
                    '10206',
                    '10207',
                ],
                "taskStatus": 'task',
                "unBlock": '1',
                "updateTime": '2021-06-19 10:53:20',
                "taskActionLists":[],
                "taskActionList":[
                    {
                        "pointId": 1000000016,
                        "action": "1_(_GR21E_000000_ffffff)",
                        "finishTime": "2021-09-08 15:00:00 / 进行中"
                    },
                    {
                        "pointId": 1000000016,
                        "action": "2_(_PL53R_000000_567456,_PL54R_000000_ffffff)",
                        "finishTime": "2021-09-08 15:00:00 / 进行中"
                    },
                    {
                        "pointId": 1000000016,
                        "action": "1_(_PR21E_000000_ffffff)",
                        "finishTime": "2021-09-08 15:00:00 / 进行中"
                    },
                    {
                        "pointId": 1000000016,
                        "action": "2_(_GL53R_000000_ffffff,_PL54R_000000_ffffff)",
                        "finishTime": ""
                    },
                    {
                        "pointId": 1000000016,
                        "action": "1_(_GR21E_000000_ffffff)",
                        "finishTime": "2021-09-08 15:00:00 / 进行中"
                    },
                    {
                        "pointId": 1000000016,
                        "action": "1_(_GR21E_000000_ffffff)",
                        "finishTime": "2021-09-08 15:00:00 / 进行中"
                    },
                    {
                        "pointId": 1000000016,
                        "action": "1_(_GR21E_000000_ffffff)",
                        "finishTime": "2021-09-08 15:00:00 / 进行中"
                    }
                ],
                "taskActionIndex": 2,
            },
                {
                "agvArea": "null",
                "agvId": 'agv005',
                "taskId": 'Task_20210619101513075',
                "taskIndex": 1,
                "moveStatus": 'stop',
                "agvStopReasonS": "STOP_CARD",
                "batteryLevel": 80,
                "headingAngle": '-90',
                "ipAddress": '127.0.0.1:47340',
                "loading": [0, 0, 1, 1, 0, 1],
                "onLine": 'on',
                "powerChargeLevelHigh": 0,
                "powerChargeLevelLow": 0,
                "powerChargeLevelOff": 0,
                "now": '10101',
                "to": "10205",
                "yet": "10203",
                "speed": 1.0,
                "taskCount": 5,
                "taskEndTime": "null",
                "taskList": [
                    '10203',
                    '10204',
                    '10205',
                    '10206',
                    '10207',
                ],
                "taskStatus": 'task',
                "unBlock": '1',
                "updateTime": '2021-06-19 10:53:20',
                "taskActionLists":[],
                "taskActionList":[
                    {
                        "pointId": 1000000016,
                        "action": "1_(_GR21E_000000_ffffff)",
                        "finishTime": "2021-09-08 15:00:00 / 进行中"
                    },
                    {
                        "pointId": 1000000016,
                        "action": "2_(_PL53R_000000_567456,_PL54R_000000_ffffff)",
                        "finishTime": "2021-09-08 15:00:00 / 进行中"
                    },
                    {
                        "pointId": 1000000016,
                        "action": "1_(_PR21E_000000_ffffff)",
                        "finishTime": "2021-09-08 15:00:00 / 进行中"
                    },
                    {
                        "pointId": 1000000016,
                        "action": "2_(_GL53R_000000_ffffff,_PL54R_000000_ffffff)",
                        "finishTime": ""
                    },
                    {
                        "pointId": 1000000016,
                        "action": "1_(_GR21E_000000_ffffff)",
                        "finishTime": "2021-09-08 15:00:00 / 进行中"
                    },
                    {
                        "pointId": 1000000016,
                        "action": "1_(_GR21E_000000_ffffff)",
                        "finishTime": "2021-09-08 15:00:00 / 进行中"
                    },
                    {
                        "pointId": 1000000016,
                        "action": "1_(_GR21E_000000_ffffff)",
                        "finishTime": "2021-09-08 15:00:00 / 进行中"
                    }
                ],
                "taskActionIndex": 2,
            },
            ]
        },
        "meta": {"msg": "地图信息成功", "status": 200}
    }
    return ret


@app.route('/getMissionList', methods=['GET', 'POST'])
def getMissionList():
    args = request.get_data()
    print(args)
    ret = {
        "data": {
            "total": 1,
            "pagenum": 0,
            "taskList": [
                {
                    "taskId": "AgvcStandby_20201019150348633",
                    "taskType": "进货、出货、充电",
                    "taskStatus": "执行中",
                    "agvId": "agv008",
                    "area": "HB-2F-45",
                    "markList": [
                        "Po-22000045"
                    ],
                    "actionList": ["無動作"],
                    "markIndex":[
                        62
                    ],
                    "markTime":[
                        "2020-10-1915:03:48"
                    ],
                    "startTime":"2020-10-1915:03:48",
                    "taskList":[
                        {
                            "dirPointId": 1000000138,
                            "tagId": "Po-138"
                        }
                    ],
                    "taskBeginTime": "2020-10-19 15:03:59",
                }
            ]
        },
        "meta": {
            "msg": "任务信息获取成功",
            "status": 200
        }
    }
    return ret


@app.route('/getAllMissionList', methods=['GET', 'POST'])
def getAllMissionList():
    args = request.get_data()
    print(args)
    ret = {
        "data": {
            "total": 1,
            "pagenum": 0,
            "taskList": [
                {
                    "taskId": "AgvcStandby_20201019150348633",
                    "taskType": "进货、出货、充电",
                    "taskStatus": "执行中",
                    "agvId": "agv008",
                    "area": "HB-2F-45",
                    "markList": [
                        "Po-22000045"
                    ],
                    "actionList": ["無動作"],
                    "markIndex":[
                        62
                    ],
                    "markTime":[
                        "2020-10-1915:03:48"
                    ],
                    "startTime":"2020-10-1915:03:48",
                    "taskList":[
                        {
                            "dirPointId": 1000000138,
                            "tagId": "Po-138"
                        }
                    ],
                    "taskBeginTime": "2020-10-19 15:03:59",
                }
            ]
        },
        "meta": {
            "msg": "任务信息获取成功",
            "status": 200
        }
    }
    return ret


@app.route('/dispatchMission', methods=['GET', 'POST'])
def dispatchMission():
    args = request.get_data()
    print(args)
    ret = {
        "data": {
        },
        "meta": {
            "msg": "任务派发成功",
            "status": 200
        }
    }
    return ret


@app.route('/taskModel', methods=['GET'])
def taskModel():
    args = request.get_data()
    print(args)
    ret = {
        "data": {
            "total": 1,
            "pagenum": 0,
            "taskModelList": [
                {
                    "id": 123,
                    "taskModelName": "task",
                    "actionList": ["1_(_GR21E_000000_ffffff)", "1_(_GR32E_000000_ffffff)", "2_(_PL53E_,_PL54R_000000_ffffff)"],
                    "markList":["105", "101", "132"],
                    "remark":"000"
                },
                {
                    "id": 456,
                    "taskModelName": "task",
                    "actionList": ["1_(_GR21E_000000_ffffff)", "2_(_PL53E_000000_ffffff,_PL54R_000000_ffffff)",  "", "2_(_PL53E_000000_ffffff,_PL54R_000000_ffffff)"],
                    "markList":["105", "101", "101", "132"],
                    "remark":"000"
                }
            ]
        },
        "meta": {
            "msg": "模板列表获取成功成功",
            "status": 200
        }
    }
    return ret


@app.route('/taskModel', methods=['DELETE'])
def taskModelDELETE():
    args = request.get_data()
    print(args)
    ret = {
        "data": {
            "id": '123123'
        },
        "meta": {
            "msg": "任务派发成功",
            "status": 200
        }
    }
    return ret


@app.route('/taskModel', methods=['POST'])
def taskModelPOST():
    args = request.get_data()
    print(args)
    ret = {
        "data": {
            "id": '123123'
        },
        "meta": {
            "msg": "任务派发成功",
            "status": 200
        }
    }
    return ret


@app.route('/taskModel', methods=['PUT'])
def taskModelPUT():
    args = request.get_data()
    print(args)
    ret = {
        "data": {
            "id": '123123'
        },
        "meta": {
            "msg": "任务派发成功",
            "status": 200
        }
    }
    return ret


@app.route('/getSystemInfo', methods=['GET'])
def getSystemInfo():
    args = request.get_data()
    print(args)
    ret = {
        "data": {
            "systemInfo": [
                {"time": "1202-06-05 22:22:22",
                    "info": "agv001开始任务 "},
                {"time": "1202-06-05 22:22:22", "info": "agv001开始任务a"},
                {"time": "1202-06-05 22:22:22", "info": "agv001开始任务"},
                {"time": "1202-06-05 22:22:22", "info": "agv001开始任务"},
                {"time": "1202-06-05 22:22:22", "info": "agv001开始任务"},
                {"time": "1202-06-05 22:22:22", "info": "agv001开始任务"},
                {"time": "1202-06-05 22:22:22", "info": "agv001开始任务"},
                {"time": "1202-06-05 22:22:22", "info": "agv001开始任务"},
                {"time": "1202-06-05 22:22:22", "info": "agv001开始任务"},
                {"time": "1202-06-05 22:22:22", "info": "agv001开始任务"},
                {"time": "1202-06-05 22:22:22", "info": "agv001开始任务"},
                {"time": "1202-06-05 22:22:22", "info": "agv001开始任务"},
                {"time": "1202-06-05 22:22:22", "info": "agv001开始任务"},
                {"time": "1202-06-05 22:22:22", "info": "agv001开始任务"},
                {"time": "1202-06-05 22:22:22", "info": "agv001开始任务"},
                {"time": "1202-06-05 22:22:22", "info": "agv001开始任务"},
                {"time": "1202-06-05 22:22:22", "info": "agv001开始任务"},
                {"time": "1202-06-05 22:22:22", "info": "agv001开始任务"},
                {"time": "1202-06-05 22:22:22", "info": "agv001开始任务"},
            ],
        },
        "meta": {
            "msg": "任务派发成功",
            "status": 200
        }
    }

    return ret


@app.route('/getTrafficInfo', methods=['GET'])
def getTrafficInfo():
    args = request.get_data()
    print(args)
    ret = {
        "data": {
            "total": 1,
            "pagenum": 0,
            "trafficControlList": [
                {
                    "controlArea": "tf01",
                    "agvEnter": ["agv001"],
                    "agvWaitEnter": ["agv002", "agv003", "agv004"],
                },
                {
                    "controlArea": "tf02",
                    "agvEnter": ["agv006"],
                    "agvWaitEnter": ["agv002", "agv003", "agv004"],
                }
            ]
        },
        "meta": {
            "msg": "交管信息获取成功",
            "status": 200
        }
    }
    return ret


@app.route('/freeControlArea', methods=['GET'])
def freeControlArea():
    args = request.get_data()
    print(args)
    ret = {
        "data": {

        },
        "meta": {
            "msg": "交管区域释放成功",
            "status": 200
        }
    }
    return ret


@app.route('/freeControlAgv', methods=['GET'])
def freeControlAgv():
    args = request.get_data()
    print(args)
    ret = {
        "data": {

        },
        "meta": {
            "msg": "agv001释放成功",
            "status": 200
        }
    }
    return ret


@app.route('/checkALLEQ/open', methods=['GET', 'POST'])
def checkALLEQopen():
    args = request.get_data()
    print(args)
    ret = {
        "data": {
        },
        "meta": {
            "msg": "打开充电检测成功",
            "status": 200
        }
    }
    return ret


@app.route('/checkALLEQ/close', methods=['GET', 'POST'])
def checkALLEQclose():
    args = request.get_data()
    print(args)
    ret = {
        "data": {
        },
        "meta": {
            "msg": "关闭充电检测成功",
            "status": 200
        }
    }
    return ret


if __name__ == "__main__":
    app.run(host="127.0.0.1", port="8999", debug=True)
