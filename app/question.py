embedded_json = []


oldpa = [{'id': 5181, 'relevance': 9, 'coherence': 8, 'fluency': 8}, {'id': 402, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 403, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 404, 'relevance': 5, 'coherence': 5, 'fluency': 5}, {'id': 400, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 401, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 5183, 'relevance': 10, 'coherence': 10, 'fluency': 10}, {'id': 430, 'relevance': 5, 'coherence': 5, 'fluency': 3}, {'id': 431, 'relevance': 9, 'coherence': 2, 'fluency': 8}, {'id': 432, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 433, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 434, 'relevance': 5, 'coherence': 5, 'fluency': 5}, {'id': 3611, 'relevance': 6, 'coherence': 5, 'fluency': 8}, {'id': 3612, 'relevance': 6, 'coherence': 6, 'fluency': 8}, {'id': 5236, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 3613, 'relevance': 6, 'coherence': 6, 'fluency': 8}, {'id': 3614, 'relevance': 6, 'coherence': 6, 'fluency': 7}, {'id': 3615, 'relevance': 7, 'coherence': 6, 'fluency': 6}, {'id': 470, 'relevance': 2, 'coherence': 2, 'fluency': 6}, {'id': 471, 'relevance': 7, 'coherence': 2, 'fluency': 2}, {'id': 472, 'relevance': 2, 'coherence': 2, 'fluency': 6}, {'id': 473, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 474, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 1316, 'relevance': 2, 'coherence': 6, 'fluency': 2}, {'id': 480, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 481, 'relevance': 4, 'coherence': 2, 'fluency': 6}, {'id': 482, 'relevance': 4, 'coherence': 6, 'fluency': 4}, {'id': 484, 'relevance': 6, 'coherence': 2, 'fluency': 2}, {'id': 1320, 'relevance': 4, 'coherence': 2, 'fluency': 4}, {'id': 483, 'relevance': 6, 'coherence': 4, 'fluency': 2}, {'id': 620, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 5173, 'relevance': 7, 'coherence': 8, 'fluency': 8}, {'id': 621, 'relevance': 3, 'coherence': 4, 'fluency': 6}, {'id': 622, 'relevance': 7, 'coherence': 8, 'fluency': 8}, {'id': 623, 'relevance': 7, 'coherence': 7, 'fluency': 8}, {'id': 624, 'relevance': 7, 'coherence': 8, 'fluency': 8}, {'id': 5178, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 629, 'relevance': 5, 'coherence': 5, 'fluency': 6}, {'id': 625, 'relevance': 5, 'coherence': 5, 'fluency': 6}, {'id': 626, 'relevance': 5, 'coherence': 6, 'fluency': 6}, {'id': 627, 'relevance': 6, 'coherence': 6, 'fluency': 7}, {'id': 628, 'relevance': 7, 'coherence': 7, 'fluency': 8}, {'id': 835, 'relevance': 5, 'coherence': 6, 'fluency': 6}, {'id': 836, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 837, 'relevance': 7, 'coherence': 6, 'fluency': 6}, {'id': 838, 'relevance': 7, 'coherence': 7, 'fluency': 8}, {'id': 5177, 'relevance': 9, 'coherence': 8, 'fluency': 9}, {'id': 839, 'relevance': 7, 'coherence': 7, 'fluency': 8}, {'id': 846, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 847, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 5182, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 845, 'relevance': 8, 'coherence': 2, 'fluency': 10}, {'id': 848, 'relevance': 2, 'coherence': 2, 'fluency': 3}, {'id': 849, 'relevance': 3, 'coherence': 10, 'fluency': 10}, {'id': 5174, 'relevance': 6, 'coherence': 6, 'fluency': 7}, {'id': 756, 'relevance': 7, 'coherence': 10, 'fluency': 2}, {'id': 757, 'relevance': 10, 'coherence': 10, 'fluency': 10}, {'id': 758, 'relevance': 7, 'coherence': 10, 'fluency': 10}, {'id': 759, 'relevance': 4, 'coherence': 10, 'fluency': 5}, {'id': 755, 'relevance': 7, 'coherence': 4, 'fluency': 7}, {'id': 460, 'relevance': 4, 'coherence': 3, 'fluency': 3}, {'id': 462, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 461, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 463, 'relevance': 2, 'coherence': 7, 'fluency': 7}, {'id': 464, 'relevance': 2, 'coherence': 7, 'fluency': 7}, {'id': 1318, 'relevance': 7, 'coherence': 7, 'fluency': 3}, {'id': 1322, 'relevance': 5, 'coherence': 5, 'fluency': 5}, {'id': 790, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 791, 'relevance': 4, 'coherence': 5, 'fluency': 4}, {'id': 792, 'relevance': 4, 'coherence': 4, 'fluency': 6}, {'id': 793, 'relevance': 6, 'coherence': 4, 'fluency': 7}, {'id': 794, 'relevance': 3, 'coherence': 5, 'fluency': 5}, {'id': 1023, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 1024, 'relevance': 2, 'coherence': 7, 'fluency': 2}, {'id': 1328, 'relevance': 2, 'coherence': 7, 'fluency': 7}, {'id': 1020, 'relevance': 2, 'coherence': 3, 'fluency': 7}, {'id': 1021, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 1022, 'relevance': 2, 'coherence': 3, 'fluency': 7}, {'id': 1323, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 465, 'relevance': 7, 'coherence': 7, 'fluency': 8}, {'id': 466, 'relevance': 8, 'coherence': 7, 'fluency': 8}, {'id': 467, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 468, 'relevance': 8, 'coherence': 7, 'fluency': 7}, {'id': 469, 'relevance': 8, 'coherence': 7, 'fluency': 8}, {'id': 1430, 'relevance': 4, 'coherence': 4, 'fluency': 3}, {'id': 1426, 'relevance': 2, 'coherence': 3, 'fluency': 3}, {'id': 1427, 'relevance': 4, 'coherence': 4, 'fluency': 3}, {'id': 1428, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 1429, 'relevance': 5, 'coherence': 4, 'fluency': 4}, {'id': 5161, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 1433, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 1431, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 1434, 'relevance': 7, 'coherence': 7, 'fluency': 8}, {'id': 1435, 'relevance': 7, 'coherence': 7, 'fluency': 8}, {'id': 5142, 'relevance': 5, 'coherence': 5, 'fluency': 5}, {'id': 1432, 'relevance': 6, 'coherence': 6, 'fluency': 7}, {'id': 5162, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 1391, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 1392, 'relevance': 4, 'coherence': 4, 'fluency': 6}, {'id': 1393, 'relevance': 3, 'coherence': 3, 'fluency': 4}, {'id': 1395, 'relevance': 10, 'coherence': 10, 'fluency': 10}, {'id': 1394, 'relevance': 7, 'coherence': 6, 'fluency': 6}, {'id': 1514, 'relevance': 3, 'coherence': 8, 'fluency': 7}, {'id': 1511, 'relevance': 4, 'coherence': 8, 'fluency': 2}, {'id': 1512, 'relevance': 4, 'coherence': 4, 'fluency': 3}, {'id': 1513, 'relevance': 3, 'coherence': 8, 'fluency': 7}, {'id': 1515, 'relevance': 8, 'coherence': 8, 'fluency': 7}, {'id': 5107, 'relevance': 7, 'coherence': 7, 'fluency': 2}, {'id': 5156, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 1471, 'relevance': 5, 'coherence': 6, 'fluency': 7}, {'id': 1472, 'relevance': 8, 'coherence': 8, 'fluency': 9}, {'id': 1473, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 1474, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 1475, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 1451, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 1452, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 1453, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 1454, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 1455, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 5152, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 5153, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 5144, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 1484, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 1481, 'relevance': 2, 'coherence': 9, 'fluency': 8}, {'id': 1482, 'relevance': 5, 'coherence': 3, 'fluency': 3}, {'id': 1483, 'relevance': 10, 'coherence': 3, 'fluency': 3}, {'id': 1485, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 1766, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 1767, 'relevance': 2, 'coherence': 3, 'fluency': 3}, {'id': 1768, 'relevance': 3, 'coherence': 3, 'fluency': 2}, {'id': 1769, 'relevance': 3, 'coherence': 4, 'fluency': 2}, {'id': 1770, 'relevance': 4, 'coherence': 3, 'fluency': 3}, {'id': 5128, 'relevance': 2, 'coherence': 2, 'fluency': 1}, {'id': 18744, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 5864, 'relevance': 7, 'coherence': 6, 'fluency': 7}, {'id': 5860, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 5861, 'relevance': 8, 'coherence': 7, 'fluency': 8}, {'id': 5862, 'relevance': 7, 'coherence': 8, 'fluency': 8}, {'id': 5863, 'relevance': 6, 'coherence': 5, 'fluency': 5}, {'id': 6090, 'relevance': 2, 'coherence': 2, 'fluency': 3}, {'id': 6091, 'relevance': 5, 'coherence': 4, 'fluency': 4}, {'id': 6092, 'relevance': 1, 'coherence': 1, 'fluency': 1}, {'id': 15876, 'relevance': 4, 'coherence': 3, 'fluency': 4}, {'id': 6093, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 6094, 'relevance': 4, 'coherence': 3, 'fluency': 4}, {'id': 18635, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 6011, 'relevance': 3, 'coherence': 7, 'fluency': 7}, {'id': 6012, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 6013, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 6014, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 6010, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 16090, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 5985, 'relevance': 5, 'coherence': 3, 'fluency': 5}, {'id': 5986, 'relevance': 8, 'coherence': 8, 'fluency': 7}, {'id': 5987, 'relevance': 7, 'coherence': 7, 'fluency': 8}, {'id': 5988, 'relevance': 9, 'coherence': 8, 'fluency': 9}, {'id': 5989, 'relevance': 5, 'coherence': 4, 'fluency': 8}, {'id': 6081, 'relevance': 2, 'coherence': 2, 'fluency': 6}, {'id': 6082, 'relevance': 6, 'coherence': 2, 'fluency': 2}, {'id': 6083, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 6084, 'relevance': 2, 'coherence': 2, 'fluency': 6}, {'id': 15885, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 6080, 'relevance': 10, 'coherence': 10, 'fluency': 10}, {'id': 5982, 'relevance': 3, 'coherence': 4, 'fluency': 4}, {'id': 5980, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 5981, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 5983, 'relevance': 8, 'coherence': 7, 'fluency': 8}, {'id': 5984, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 18451, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 18773, 'relevance': 4, 'coherence': 1, 'fluency': 1}, {'id': 6057, 'relevance': 1, 'coherence': 2, 'fluency': 2}, {'id': 6058, 'relevance': 3, 'coherence': 2, 'fluency': 1}, {'id': 6055, 'relevance': 1, 'coherence': 2, 'fluency': 2}, {'id': 6056, 'relevance': 2, 'coherence': 2, 'fluency': 3}, {'id': 6059, 'relevance': 2, 'coherence': 4, 'fluency': 1}, {'id': 15761, 'relevance': 8, 'coherence': 6, 'fluency': 8}, {'id': 6250, 'relevance': 6, 'coherence': 4, 'fluency': 6}, {'id': 6251, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 6252, 'relevance': 4, 'coherence': 8, 'fluency': 8}, {'id': 6253, 'relevance': 8, 'coherence': 4, 'fluency': 6}, {'id': 6254, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 15834, 'relevance': 3, 'coherence': 4, 'fluency': 3}, {'id': 6340, 'relevance': 1, 'coherence': 2, 'fluency': 1}, {'id': 6341, 'relevance': 1, 'coherence': 2, 'fluency': 1}, {'id': 6342, 'relevance': 4, 'coherence': 2, 'fluency': 1}, {'id': 6343, 'relevance': 3, 'coherence': 2, 'fluency': 3}, {'id': 6344, 'relevance': 3, 'coherence': 2, 'fluency': 3}, {'id': 6270, 'relevance': 3, 'coherence': 5, 'fluency': 3}, {'id': 6271, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 6272, 'relevance': 3, 'coherence': 3, 'fluency': 1}, {'id': 6273, 'relevance': 3, 'coherence': 2, 'fluency': 3}, {'id': 15980, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 6274, 'relevance': 2, 'coherence': 3, 'fluency': 2}, {'id': 6165, 'relevance': 2, 'coherence': 2, 'fluency': 9}, {'id': 16036, 'relevance': 9, 'coherence': 8, 'fluency': 8}, {'id': 6166, 'relevance': 5, 'coherence': 3, 'fluency': 3}, {'id': 6167, 'relevance': 4, 'coherence': 3, 'fluency': 4}, {'id': 6168, 'relevance': 5, 'coherence': 6, 'fluency': 6}, {'id': 6169, 'relevance': 9, 'coherence': 10, 'fluency': 2}, {'id': 6174, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 6172, 'relevance': 3, 'coherence': 7, 'fluency': 7}, {'id': 6170, 'relevance': 2, 'coherence': 7, 'fluency': 2}, {'id': 16037, 'relevance': 8, 'coherence': 3, 'fluency': 3}, {'id': 6171, 'relevance': 3, 'coherence': 7, 'fluency': 3}, {'id': 6173, 'relevance': 4, 'coherence': 3, 'fluency': 8}, {'id': 16204, 'relevance': 2, 'coherence': 2, 'fluency': 3}, {'id': 6210, 'relevance': 7, 'coherence': 6, 'fluency': 6}, {'id': 6211, 'relevance': 6, 'coherence': 8, 'fluency': 8}, {'id': 6212, 'relevance': 6, 'coherence': 5, 'fluency': 8}, {'id': 6213, 'relevance': 8, 'coherence': 9, 'fluency': 9}, {'id': 6214, 'relevance': 6, 'coherence': 7, 'fluency': 8}, {'id': 6149, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 6147, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 6148, 'relevance': 9, 'coherence': 8, 'fluency': 8}, {'id': 6145, 'relevance': 6, 'coherence': 6, 'fluency': 5}, {'id': 18343, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 6146, 'relevance': 8, 'coherence': 8, 'fluency': 9}, {'id': 6140, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 6141, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 6142, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 6143, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 18582, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 6144, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 6312, 'relevance': 1, 'coherence': 2, 'fluency': 2}, {'id': 18678, 'relevance': 4, 'coherence': 4, 'fluency': 6}, {'id': 6310, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 6311, 'relevance': 4, 'coherence': 4, 'fluency': 2}, {'id': 6313, 'relevance': 6, 'coherence': 6, 'fluency': 4}, {'id': 6314, 'relevance': 2, 'coherence': 6, 'fluency': 10}, {'id': 6470, 'relevance': 8, 'coherence': 6, 'fluency': 7}, {'id': 15720, 'relevance': 7, 'coherence': 7, 'fluency': 8}, {'id': 6474, 'relevance': 7, 'coherence': 7, 'fluency': 8}, {'id': 6473, 'relevance': 8, 'coherence': 8, 'fluency': 7}, {'id': 6471, 'relevance': 8, 'coherence': 7, 'fluency': 6}, {'id': 6472, 'relevance': 8, 'coherence': 8, 'fluency': 7}, {'id': 8061, 'relevance': 7, 'coherence': 6, 'fluency': 6}, {'id': 8062, 'relevance': 6, 'coherence': 7, 'fluency': 7}, {'id': 8063, 'relevance': 8, 'coherence': 7, 'fluency': 7}, {'id': 8064, 'relevance': 9, 'coherence': 9, 'fluency': 8}, {'id': 12321, 'relevance': 9, 'coherence': 8, 'fluency': 9}, {'id': 8060, 'relevance': 6, 'coherence': 5, 'fluency': 7}, {'id': 15737, 'relevance': 3, 'coherence': 2, 'fluency': 2}, {'id': 6405, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 6406, 'relevance': 3, 'coherence': 2, 'fluency': 3}, {'id': 6407, 'relevance': 2, 'coherence': 2, 'fluency': 3}, {'id': 6408, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 6409, 'relevance': 3, 'coherence': 2, 'fluency': 3}, {'id': 6505, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 6506, 'relevance': 9, 'coherence': 3, 'fluency': 6}, {'id': 6507, 'relevance': 3, 'coherence': 6, 'fluency': 3}, {'id': 6508, 'relevance': 3, 'coherence': 9, 'fluency': 3}, {'id': 16061, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 6509, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 16206, 'relevance': 1, 'coherence': 3, 'fluency': 3}, {'id': 6480, 'relevance': 1, 'coherence': 1, 'fluency': 1}, {'id': 6481, 'relevance': 2, 'coherence': 1, 'fluency': 2}, {'id': 6482, 'relevance': 1, 'coherence': 2, 'fluency': 3}, {'id': 6483, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 6484, 'relevance': 3, 'coherence': 3, 'fluency': 2}, {'id': 16244, 'relevance': 4, 'coherence': 4, 'fluency': 5}, {'id': 6490, 'relevance': 5, 'coherence': 3, 'fluency': 5}, {'id': 6491, 'relevance': 3, 'coherence': 3, 'fluency': 4}, {'id': 6492, 'relevance': 1, 'coherence': 1, 'fluency': 4}, {'id': 6493, 'relevance': 3, 'coherence': 5, 'fluency': 3}, {'id': 6494, 'relevance': 2, 'coherence': 3, 'fluency': 4}, {'id': 5163, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 2481, 'relevance': 8, 'coherence': 8, 'fluency': 6}, {'id': 2482, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 2483, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 2484, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 2485, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 6373, 'relevance': 4, 'coherence': 8, 'fluency': 2}, {'id': 6374, 'relevance': 4, 'coherence': 4, 'fluency': 6}, {'id': 18722, 'relevance': 3, 'coherence': 2, 'fluency': 1}, {'id': 6370, 'relevance': 2, 'coherence': 4, 'fluency': 2}, {'id': 6372, 'relevance': 6, 'coherence': 4, 'fluency': 2}, {'id': 6371, 'relevance': 2, 'coherence': 2, 'fluency': 6}, {'id': 6440, 'relevance': 4, 'coherence': 4, 'fluency': 5}, {'id': 6443, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 6441, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 6442, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 6444, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 18727, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 6615, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 6616, 'relevance': 6, 'coherence': 6, 'fluency': 8}, {'id': 15758, 'relevance': 8, 'coherence': 6, 'fluency': 8}, {'id': 6618, 'relevance': 3, 'coherence': 4, 'fluency': 4}, {'id': 6617, 'relevance': 6, 'coherence': 6, 'fluency': 8}, {'id': 6619, 'relevance': 6, 'coherence': 8, 'fluency': 8}, {'id': 6635, 'relevance': 7, 'coherence': 7, 'fluency': 8}, {'id': 6636, 'relevance': 2, 'coherence': 4, 'fluency': 9}, {'id': 6637, 'relevance': 10, 'coherence': 9, 'fluency': 9}, {'id': 6638, 'relevance': 8, 'coherence': 8, 'fluency': 9}, {'id': 6639, 'relevance': 7, 'coherence': 4, 'fluency': 10}, {'id': 18563, 'relevance': 2, 'coherence': 3, 'fluency': 10}, {'id': 2651, 'relevance': 5, 'coherence': 5, 'fluency': 6}, {'id': 2652, 'relevance': 8, 'coherence': 7, 'fluency': 8}, {'id': 2653, 'relevance': 6, 'coherence': 5, 'fluency': 7}, {'id': 2654, 'relevance': 8, 'coherence': 7, 'fluency': 6}, {'id': 2655, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 5158, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 6758, 'relevance': 0, 'coherence': 0, 'fluency': 0}, {'id': 6757, 'relevance': 6, 'coherence': 9, 'fluency': 6}, {'id': 16058, 'relevance': 9, 'coherence': 9, 'fluency': 6}, {'id': 6755, 'relevance': 3, 'coherence': 3, 'fluency': 9}, {'id': 6756, 'relevance': 3, 'coherence': 3, 'fluency': 9}, {'id': 6759, 'relevance': 9, 'coherence': 9, 'fluency': 6}, {'id': 2646, 'relevance': 8, 'coherence': 7, 'fluency': 8}, {'id': 2647, 'relevance': 7, 'coherence': 7, 'fluency': 9}, {'id': 2648, 'relevance': 7, 'coherence': 5, 'fluency': 8}, {'id': 2649, 'relevance': 7, 'coherence': 7, 'fluency': 8}, {'id': 2650, 'relevance': 7, 'coherence': 8, 'fluency': 8}, {'id': 5159, 'relevance': 5, 'coherence': 7, 'fluency': 6}, {'id': 18280, 'relevance': 7, 'coherence': 8, 'fluency': 8}, {'id': 6657, 'relevance': 7, 'coherence': 8, 'fluency': 8}, {'id': 6658, 'relevance': 6, 'coherence': 8, 'fluency': 8}, {'id': 6659, 'relevance': 9, 'coherence': 9, 'fluency': 8}, {'id': 6655, 'relevance': 6, 'coherence': 8, 'fluency': 8}, {'id': 6656, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 6713, 'relevance': 10, 'coherence': 8, 'fluency': 8}, {'id': 6714, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 18310, 'relevance': 8, 'coherence': 9, 'fluency': 8}, {'id': 6710, 'relevance': 9, 'coherence': 8, 'fluency': 7}, {'id': 6711, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 6712, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 18450, 'relevance': 3, 'coherence': 3, 'fluency': 5}, {'id': 6725, 'relevance': 7, 'coherence': 7, 'fluency': 5}, {'id': 6726, 'relevance': 6, 'coherence': 8, 'fluency': 6}, {'id': 6727, 'relevance': 6, 'coherence': 4, 'fluency': 5}, {'id': 6728, 'relevance': 7, 'coherence': 5, 'fluency': 5}, {'id': 6729, 'relevance': 5, 'coherence': 4, 'fluency': 5}, {'id': 5160, 'relevance': 3, 'coherence': 3, 'fluency': 4}, {'id': 2643, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 2644, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 2645, 'relevance': 8, 'coherence': 7, 'fluency': 7}, {'id': 2641, 'relevance': 7, 'coherence': 7, 'fluency': 5}, {'id': 2642, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 6745, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 6746, 'relevance': 6, 'coherence': 7, 'fluency': 7}, {'id': 6747, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 6749, 'relevance': 8, 'coherence': 6, 'fluency': 8}, {'id': 18640, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 6748, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 2636, 'relevance': 5, 'coherence': 5, 'fluency': 7}, {'id': 2637, 'relevance': 10, 'coherence': 10, 'fluency': 10}, {'id': 2638, 'relevance': 5, 'coherence': 5, 'fluency': 7}, {'id': 2639, 'relevance': 9, 'coherence': 9, 'fluency': 10}, {'id': 2640, 'relevance': 6, 'coherence': 6, 'fluency': 7}, {'id': 5164, 'relevance': 10, 'coherence': 10, 'fluency': 10}, {'id': 6630, 'relevance': 4, 'coherence': 4, 'fluency': 2}, {'id': 6631, 'relevance': 1, 'coherence': 1, 'fluency': 1}, {'id': 6632, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 6633, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 6634, 'relevance': 4, 'coherence': 6, 'fluency': 6}, {'id': 18718, 'relevance': 6, 'coherence': 4, 'fluency': 6}, {'id': 6800, 'relevance': 7, 'coherence': 6, 'fluency': 7}, {'id': 6802, 'relevance': 7, 'coherence': 6, 'fluency': 9}, {'id': 16040, 'relevance': 7, 'coherence': 8, 'fluency': 6}, {'id': 6801, 'relevance': 7, 'coherence': 6, 'fluency': 7}, {'id': 6803, 'relevance': 9, 'coherence': 8, 'fluency': 9}, {'id': 6804, 'relevance': 6, 'coherence': 7, 'fluency': 8}, {'id': 2762, 'relevance': 7, 'coherence': 6, 'fluency': 8}, {'id': 2763, 'relevance': 6, 'coherence': 6, 'fluency': 5}, {'id': 5134, 'relevance': 7, 'coherence': 6, 'fluency': 8}, {'id': 2764, 'relevance': 10, 'coherence': 8, 'fluency': 6}, {'id': 2765, 'relevance': 7, 'coherence': 8, 'fluency': 8}, {'id': 2761, 'relevance': 8, 'coherence': 6, 'fluency': 7}, {'id': 6780, 'relevance': 10, 'coherence': 8, 'fluency': 9}, {'id': 15782, 'relevance': 9, 'coherence': 9, 'fluency': 10}, {'id': 6781, 'relevance': 9, 'coherence': 8, 'fluency': 2}, {'id': 6782, 'relevance': 2, 'coherence': 10, 'fluency': 10}, {'id': 6783, 'relevance': 3, 'coherence': 2, 'fluency': 3}, {'id': 6784, 'relevance': 2, 'coherence': 7, 'fluency': 2}, {'id': 2811, 'relevance': 7, 'coherence': 7, 'fluency': 6}, {'id': 2812, 'relevance': 6, 'coherence': 4, 'fluency': 4}, {'id': 2815, 'relevance': 8, 'coherence': 7, 'fluency': 8}, {'id': 5137, 'relevance': 9, 'coherence': 8, 'fluency': 8}, {'id': 2813, 'relevance': 3, 'coherence': 4, 'fluency': 2}, {'id': 2814, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 6785, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 6786, 'relevance': 7, 'coherence': 6, 'fluency': 6}, {'id': 6787, 'relevance': 7, 'coherence': 7, 'fluency': 6}, {'id': 6788, 'relevance': 5, 'coherence': 5, 'fluency': 5}, {'id': 6789, 'relevance': 7, 'coherence': 7, 'fluency': 6}, {'id': 15787, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 15754, 'relevance': 7, 'coherence': 6, 'fluency': 6}, {'id': 6810, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 6811, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 6812, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 6813, 'relevance': 6, 'coherence': 5, 'fluency': 6}, {'id': 6814, 'relevance': 8, 'coherence': 7, 'fluency': 8}, {'id': 5149, 'relevance': 6, 'coherence': 6, 'fluency': 7}, {'id': 3206, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 3207, 'relevance': 6, 'coherence': 6, 'fluency': 7}, {'id': 3208, 'relevance': 6, 'coherence': 7, 'fluency': 6}, {'id': 3209, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 3210, 'relevance': 6, 'coherence': 6, 'fluency': 7}, {'id': 3116, 'relevance': 2, 'coherence': 3, 'fluency': 2}, {'id': 3117, 'relevance': 1, 'coherence': 2, 'fluency': 2}, {'id': 5201, 'relevance': 3, 'coherence': 2, 'fluency': 3}, {'id': 3118, 'relevance': 2, 'coherence': 2, 'fluency': 1}, {'id': 3119, 'relevance': 2, 'coherence': 2, 'fluency': 3}, {'id': 3120, 'relevance': 2, 'coherence': 4, 'fluency': 3}, {'id': 5212, 'relevance': 3, 'coherence': 2, 'fluency': 3}, {'id': 5213, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 3171, 'relevance': 3, 'coherence': 4, 'fluency': 3}, {'id': 3172, 'relevance': 3, 'coherence': 2, 'fluency': 4}, {'id': 3173, 'relevance': 3, 'coherence': 4, 'fluency': 3}, {'id': 3174, 'relevance': 4, 'coherence': 2, 'fluency': 2}, {'id': 3175, 'relevance': 3, 'coherence': 2, 'fluency': 3}, {'id': 5214, 'relevance': 3, 'coherence': 2, 'fluency': 1}, {'id': 3107, 'relevance': 10, 'coherence': 9, 'fluency': 9}, {'id': 3106, 'relevance': 7, 'coherence': 8, 'fluency': 7}, {'id': 3108, 'relevance': 4, 'coherence': 6, 'fluency': 5}, {'id': 3109, 'relevance': 7, 'coherence': 6, 'fluency': 9}, {'id': 3110, 'relevance': 5, 'coherence': 7, 'fluency': 6}, {'id': 5216, 'relevance': 3, 'coherence': 4, 'fluency': 4}, {'id': 6971, 'relevance': 8, 'coherence': 9, 'fluency': 8}, {'id': 18304, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 6970, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 6972, 'relevance': 7, 'coherence': 7, 'fluency': 8}, {'id': 6973, 'relevance': 8, 'coherence': 7, 'fluency': 6}, {'id': 6974, 'relevance': 7, 'coherence': 6, 'fluency': 6}, {'id': 7030, 'relevance': 0, 'coherence': 0, 'fluency': 0}, {'id': 7031, 'relevance': 0, 'coherence': 0, 'fluency': 0}, {'id': 7032, 'relevance': 0, 'coherence': 0, 'fluency': 0}, {'id': 7033, 'relevance': 0, 'coherence': 0, 'fluency': 0}, {'id': 7034, 'relevance': 0, 'coherence': 0, 'fluency': 0}, {'id': 16202, 'relevance': 0, 'coherence': 0, 'fluency': 0}, {'id': 5102, 'relevance': 2, 'coherence': 4, 'fluency': 5}, {'id': 3386, 'relevance': 5, 'coherence': 4, 'fluency': 6}, {'id': 3387, 'relevance': 3, 'coherence': 4, 'fluency': 6}, {'id': 3388, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 3389, 'relevance': 6, 'coherence': 7, 'fluency': 6}, {'id': 3390, 'relevance': 5, 'coherence': 7, 'fluency': 6}, {'id': 3406, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 3407, 'relevance': 2, 'coherence': 3, 'fluency': 2}, {'id': 3408, 'relevance': 1, 'coherence': 1, 'fluency': 2}, {'id': 3409, 'relevance': 2, 'coherence': 2, 'fluency': 1}, {'id': 5097, 'relevance': 2, 'coherence': 1, 'fluency': 1}, {'id': 3410, 'relevance': 1, 'coherence': 2, 'fluency': 1}, {'id': 5127, 'relevance': 7, 'coherence': 4, 'fluency': 7}, {'id': 3411, 'relevance': 8, 'coherence': 6, 'fluency': 7}, {'id': 3412, 'relevance': 7, 'coherence': 8, 'fluency': 10}, {'id': 3413, 'relevance': 4, 'coherence': 6, 'fluency': 7}, {'id': 3414, 'relevance': 6, 'coherence': 8, 'fluency': 8}, {'id': 3415, 'relevance': 6, 'coherence': 7, 'fluency': 9}, {'id': 5109, 'relevance': 10, 'coherence': 10, 'fluency': 7}, {'id': 3371, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 3372, 'relevance': 2, 'coherence': 6, 'fluency': 2}, {'id': 3373, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 3374, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 3375, 'relevance': 2, 'coherence': 7, 'fluency': 7}, {'id': 5122, 'relevance': 6, 'coherence': 7, 'fluency': 6}, {'id': 3416, 'relevance': 6, 'coherence': 8, 'fluency': 8}, {'id': 3417, 'relevance': 6, 'coherence': 3, 'fluency': 3}, {'id': 3418, 'relevance': 6, 'coherence': 5, 'fluency': 4}, {'id': 3420, 'relevance': 6, 'coherence': 7, 'fluency': 5}, {'id': 3419, 'relevance': 7, 'coherence': 6, 'fluency': 5}, {'id': 3357, 'relevance': 9, 'coherence': 8, 'fluency': 9}, {'id': 5187, 'relevance': 2, 'coherence': 10, 'fluency': 2}, {'id': 3356, 'relevance': 10, 'coherence': 9, 'fluency': 10}, {'id': 3358, 'relevance': 8, 'coherence': 10, 'fluency': 9}, {'id': 3359, 'relevance': 8, 'coherence': 8, 'fluency': 9}, {'id': 3360, 'relevance': 10, 'coherence': 9, 'fluency': 10}, {'id': 3376, 'relevance': 0, 'coherence': 0, 'fluency': 0}, {'id': 3377, 'relevance': 0, 'coherence': 0, 'fluency': 0}, {'id': 3378, 'relevance': 0, 'coherence': 0, 'fluency': 0}, {'id': 3379, 'relevance': 0, 'coherence': 0, 'fluency': 0}, {'id': 3380, 'relevance': 0, 'coherence': 0, 'fluency': 0}, {'id': 5223, 'relevance': 0, 'coherence': 0, 'fluency': 0}, {'id': 7017, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 7018, 'relevance': 9, 'coherence': 8, 'fluency': 8}, {'id': 7019, 'relevance': 6, 'coherence': 7, 'fluency': 7}, {'id': 15973, 'relevance': 7, 'coherence': 8, 'fluency': 7}, {'id': 7015, 'relevance': 3, 'coherence': 6, 'fluency': 5}, {'id': 7016, 'relevance': 5, 'coherence': 7, 'fluency': 6}, {'id': 7080, 'relevance': 5, 'coherence': 7, 'fluency': 5}, {'id': 7081, 'relevance': 10, 'coherence': 3, 'fluency': 5}, {'id': 7082, 'relevance': 5, 'coherence': 5, 'fluency': 7}, {'id': 7083, 'relevance': 5, 'coherence': 7, 'fluency': 5}, {'id': 7084, 'relevance': 7, 'coherence': 5, 'fluency': 7}, {'id': 16208, 'relevance': 5, 'coherence': 5, 'fluency': 7}, {'id': 3391, 'relevance': 5, 'coherence': 4, 'fluency': 5}, {'id': 3392, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 3393, 'relevance': 6, 'coherence': 6, 'fluency': 3}, {'id': 3394, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 3395, 'relevance': 8, 'coherence': 7, 'fluency': 8}, {'id': 5147, 'relevance': 3, 'coherence': 3, 'fluency': 6}, {'id': 3464, 'relevance': 2, 'coherence': 1, 'fluency': 1}, {'id': 3465, 'relevance': 2, 'coherence': 1, 'fluency': 1}, {'id': 5123, 'relevance': 2, 'coherence': 2, 'fluency': 1}, {'id': 3461, 'relevance': 1, 'coherence': 1, 'fluency': 1}, {'id': 3462, 'relevance': 1, 'coherence': 3, 'fluency': 2}, {'id': 3463, 'relevance': 3, 'coherence': 2, 'fluency': 2}, {'id': 3521, 'relevance': 1, 'coherence': 2, 'fluency': 2}, {'id': 3522, 'relevance': 3, 'coherence': 2, 'fluency': 2}, {'id': 3525, 'relevance': 3, 'coherence': 2, 'fluency': 1}, {'id': 5115, 'relevance': 2, 'coherence': 2, 'fluency': 1}, {'id': 3523, 'relevance': 1, 'coherence': 2, 'fluency': 1}, {'id': 3524, 'relevance': 1, 'coherence': 1, 'fluency': 2}, {'id': 3681, 'relevance': 2, 'coherence': 3, 'fluency': 1}, {'id': 3685, 'relevance': 1, 'coherence': 2, 'fluency': 2}, {'id': 3682, 'relevance': 4, 'coherence': 2, 'fluency': 1}, {'id': 3683, 'relevance': 1, 'coherence': 1, 'fluency': 1}, {'id': 3684, 'relevance': 1, 'coherence': 1, 'fluency': 3}, {'id': 5220, 'relevance': 3, 'coherence': 2, 'fluency': 1}, {'id': 3541, 'relevance': 1, 'coherence': 2, 'fluency': 2}, {'id': 3542, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 3543, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 3544, 'relevance': 4, 'coherence': 2, 'fluency': 1}, {'id': 3545, 'relevance': 1, 'coherence': 3, 'fluency': 2}, {'id': 5117, 'relevance': 3, 'coherence': 3, 'fluency': 1}, {'id': 3677, 'relevance': 9, 'coherence': 8, 'fluency': 9}, {'id': 5224, 'relevance': 9, 'coherence': 8, 'fluency': 8}, {'id': 3676, 'relevance': 6, 'coherence': 8, 'fluency': 7}, {'id': 3678, 'relevance': 7, 'coherence': 8, 'fluency': 8}, {'id': 3679, 'relevance': 8, 'coherence': 7, 'fluency': 8}, {'id': 3680, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 3608, 'relevance': 8, 'coherence': 7, 'fluency': 7}, {'id': 5257, 'relevance': 9, 'coherence': 8, 'fluency': 8}, {'id': 3606, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 3607, 'relevance': 4, 'coherence': 2, 'fluency': 2}, {'id': 3609, 'relevance': 10, 'coherence': 2, 'fluency': 10}, {'id': 3610, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 15702, 'relevance': 6, 'coherence': 8, 'fluency': 7}, {'id': 7140, 'relevance': 8, 'coherence': 6, 'fluency': 7}, {'id': 7141, 'relevance': 9, 'coherence': 8, 'fluency': 8}, {'id': 7142, 'relevance': 9, 'coherence': 8, 'fluency': 7}, {'id': 7143, 'relevance': 9, 'coherence': 10, 'fluency': 10}, {'id': 7144, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 3642, 'relevance': 1, 'coherence': 2, 'fluency': 1}, {'id': 3643, 'relevance': 1, 'coherence': 1, 'fluency': 1}, {'id': 3645, 'relevance': 2, 'coherence': 1, 'fluency': 2}, {'id': 3644, 'relevance': 3, 'coherence': 1, 'fluency': 2}, {'id': 3641, 'relevance': 2, 'coherence': 1, 'fluency': 2}, {'id': 5215, 'relevance': 2, 'coherence': 1, 'fluency': 2}, {'id': 3536, 'relevance': 8, 'coherence': 7, 'fluency': 7}, {'id': 3537, 'relevance': 8, 'coherence': 6, 'fluency': 6}, {'id': 3538, 'relevance': 7, 'coherence': 5, 'fluency': 8}, {'id': 3539, 'relevance': 9, 'coherence': 7, 'fluency': 6}, {'id': 5204, 'relevance': 7, 'coherence': 6, 'fluency': 7}, {'id': 3540, 'relevance': 9, 'coherence': 7, 'fluency': 8}, {'id': 5264, 'relevance': 6, 'coherence': 6, 'fluency': 8}, {'id': 3616, 'relevance': 5, 'coherence': 5, 'fluency': 6}, {'id': 3617, 'relevance': 5, 'coherence': 6, 'fluency': 7}, {'id': 3618, 'relevance': 7, 'coherence': 7, 'fluency': 8}, {'id': 3619, 'relevance': 7, 'coherence': 7, 'fluency': 8}, {'id': 3620, 'relevance': 6, 'coherence': 5, 'fluency': 7}, {'id': 5207, 'relevance': 0, 'coherence': 0, 'fluency': 0}, {'id': 3662, 'relevance': 0, 'coherence': 0, 'fluency': 0}, {'id': 3661, 'relevance': 1, 'coherence': 1, 'fluency': 1}, {'id': 3663, 'relevance': 1, 'coherence': 1, 'fluency': 1}, {'id': 3664, 'relevance': 1, 'coherence': 1, 'fluency': 1}, {'id': 3665, 'relevance': 1, 'coherence': 1, 'fluency': 1}, {'id': 3901, 'relevance': 4, 'coherence': 5, 'fluency': 7}, {'id': 3902, 'relevance': 7, 'coherence': 8, 'fluency': 7}, {'id': 5251, 'relevance': 5, 'coherence': 7, 'fluency': 6}, {'id': 3904, 'relevance': 8, 'coherence': 8, 'fluency': 7}, {'id': 3905, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 3903, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 7352, 'relevance': 0, 'coherence': 0, 'fluency': 0}, {'id': 18613, 'relevance': 8, 'coherence': 6, 'fluency': 6}, {'id': 7350, 'relevance': 6, 'coherence': 6, 'fluency': 8}, {'id': 7351, 'relevance': 8, 'coherence': 6, 'fluency': 8}, {'id': 7353, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 7354, 'relevance': 8, 'coherence': 8, 'fluency': 6}, {'id': 7335, 'relevance': 10, 'coherence': 10, 'fluency': 10}, {'id': 7336, 'relevance': 10, 'coherence': 10, 'fluency': 10}, {'id': 7337, 'relevance': 10, 'coherence': 6, 'fluency': 2}, {'id': 15916, 'relevance': 10, 'coherence': 10, 'fluency': 2}, {'id': 7338, 'relevance': 2, 'coherence': 2, 'fluency': 7}, {'id': 7339, 'relevance': 2, 'coherence': 2, 'fluency': 7}, {'id': 3692, 'relevance': 6, 'coherence': 4, 'fluency': 4}, {'id': 3693, 'relevance': 4, 'coherence': 2, 'fluency': 4}, {'id': 3694, 'relevance': 8, 'coherence': 4, 'fluency': 6}, {'id': 3695, 'relevance': 6, 'coherence': 2, 'fluency': 4}, {'id': 5196, 'relevance': 4, 'coherence': 4, 'fluency': 6}, {'id': 3691, 'relevance': 4, 'coherence': 2, 'fluency': 4}, {'id': 3879, 'relevance': 4, 'coherence': 5, 'fluency': 5}, {'id': 3877, 'relevance': 6, 'coherence': 6, 'fluency': 8}, {'id': 5157, 'relevance': 5, 'coherence': 5, 'fluency': 6}, {'id': 3876, 'relevance': 5, 'coherence': 5, 'fluency': 6}, {'id': 3878, 'relevance': 7, 'coherence': 6, 'fluency': 6}, {'id': 3880, 'relevance': 5, 'coherence': 6, 'fluency': 6}, {'id': 5143, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 3766, 'relevance': 9, 'coherence': 6, 'fluency': 8}, {'id': 3767, 'relevance': 6, 'coherence': 5, 'fluency': 6}, {'id': 3768, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 3769, 'relevance': 4, 'coherence': 4, 'fluency': 5}, {'id': 3770, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 4141, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 5155, 'relevance': 8, 'coherence': 8, 'fluency': 7}, {'id': 4142, 'relevance': 2, 'coherence': 3, 'fluency': 10}, {'id': 4143, 'relevance': 2, 'coherence': 5, 'fluency': 3}, {'id': 4144, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 4145, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 5169, 'relevance': 6, 'coherence': 7, 'fluency': 7}, {'id': 3966, 'relevance': 6, 'coherence': 6, 'fluency': 7}, {'id': 3967, 'relevance': 8, 'coherence': 8, 'fluency': 9}, {'id': 3968, 'relevance': 8, 'coherence': 7, 'fluency': 7}, {'id': 3969, 'relevance': 7, 'coherence': 7, 'fluency': 8}, {'id': 3970, 'relevance': 7, 'coherence': 8, 'fluency': 7}, {'id': 4148, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 5141, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 4146, 'relevance': 4, 'coherence': 4, 'fluency': 5}, {'id': 4147, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 4149, 'relevance': 9, 'coherence': 7, 'fluency': 9}, {'id': 4150, 'relevance': 8, 'coherence': 7, 'fluency': 8}, {'id': 7460, 'relevance': 1, 'coherence': 1, 'fluency': 1}, {'id': 7461, 'relevance': 4, 'coherence': 5, 'fluency': 5}, {'id': 7462, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 7463, 'relevance': 3, 'coherence': 2, 'fluency': 2}, {'id': 7464, 'relevance': 2, 'coherence': 3, 'fluency': 2}, {'id': 18820, 'relevance': 5, 'coherence': 5, 'fluency': 5}, {'id': 15985, 'relevance': 8, 'coherence': 8, 'fluency': 7}, {'id': 7608, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 7609, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 7607, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 7605, 'relevance': 6, 'coherence': 5, 'fluency': 5}, {'id': 7606, 'relevance': 7, 'coherence': 8, 'fluency': 8}, {'id': 7640, 'relevance': 2, 'coherence': 3, 'fluency': 1}, {'id': 7641, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 7642, 'relevance': 4, 'coherence': 4, 'fluency': 6}, {'id': 7643, 'relevance': 7, 'coherence': 4, 'fluency': 6}, {'id': 7644, 'relevance': 6, 'coherence': 5, 'fluency': 6}, {'id': 10040, 'relevance': 4, 'coherence': 7, 'fluency': 7}, {'id': 7780, 'relevance': 3, 'coherence': 4, 'fluency': 4}, {'id': 12319, 'relevance': 6, 'coherence': 7, 'fluency': 7}, {'id': 7782, 'relevance': 6, 'coherence': 6, 'fluency': 8}, {'id': 7783, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 7784, 'relevance': 6, 'coherence': 8, 'fluency': 8}, {'id': 7781, 'relevance': 7, 'coherence': 8, 'fluency': 8}, {'id': 7775, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 7776, 'relevance': 8, 'coherence': 8, 'fluency': 6}, {'id': 7777, 'relevance': 6, 'coherence': 8, 'fluency': 6}, {'id': 7778, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 7779, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 15949, 'relevance': 8, 'coherence': 6, 'fluency': 6}, {'id': 4522, 'relevance': 4, 'coherence': 2, 'fluency': 2}, {'id': 4524, 'relevance': 4, 'coherence': 4, 'fluency': 2}, {'id': 4521, 'relevance': 2, 'coherence': 4, 'fluency': 2}, {'id': 4525, 'relevance': 2, 'coherence': 2, 'fluency': 6}, {'id': 5105, 'relevance': 2, 'coherence': 2, 'fluency': 4}, {'id': 4523, 'relevance': 2, 'coherence': 4, 'fluency': 4}, {'id': 18666, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 7805, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 7806, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 7807, 'relevance': 8, 'coherence': 8, 'fluency': 7}, {'id': 7808, 'relevance': 6, 'coherence': 7, 'fluency': 8}, {'id': 7809, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 7771, 'relevance': 8, 'coherence': 8, 'fluency': 7}, {'id': 7772, 'relevance': 7, 'coherence': 6, 'fluency': 7}, {'id': 15793, 'relevance': 7, 'coherence': 8, 'fluency': 8}, {'id': 7773, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 7770, 'relevance': 7, 'coherence': 8, 'fluency': 7}, {'id': 7774, 'relevance': 7, 'coherence': 7, 'fluency': 6}, {'id': 15615, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 7841, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 7840, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 7842, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 7843, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 7844, 'relevance': 10, 'coherence': 10, 'fluency': 6}, {'id': 7936, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 7939, 'relevance': 4, 'coherence': 4, 'fluency': 3}, {'id': 15686, 'relevance': 1, 'coherence': 2, 'fluency': 2}, {'id': 7935, 'relevance': 2, 'coherence': 3, 'fluency': 3}, {'id': 7937, 'relevance': 2, 'coherence': 2, 'fluency': 3}, {'id': 7938, 'relevance': 2, 'coherence': 4, 'fluency': 2}, {'id': 7871, 'relevance': 10, 'coherence': 10, 'fluency': 10}, {'id': 15742, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 7870, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 7873, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 7874, 'relevance': 3, 'coherence': 2, 'fluency': 2}, {'id': 7872, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 18514, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 7919, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 7915, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 7917, 'relevance': 5, 'coherence': 5, 'fluency': 6}, {'id': 7918, 'relevance': 7, 'coherence': 6, 'fluency': 6}, {'id': 7916, 'relevance': 6, 'coherence': 6, 'fluency': 7}, {'id': 8091, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 16106, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 8090, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 8092, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 8093, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 8094, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 16232, 'relevance': 6, 'coherence': 6, 'fluency': 5}, {'id': 8215, 'relevance': 5, 'coherence': 6, 'fluency': 5}, {'id': 8216, 'relevance': 6, 'coherence': 6, 'fluency': 7}, {'id': 8217, 'relevance': 7, 'coherence': 8, 'fluency': 6}, {'id': 8218, 'relevance': 7, 'coherence': 6, 'fluency': 8}, {'id': 8219, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 16188, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 8180, 'relevance': 6, 'coherence': 8, 'fluency': 6}, {'id': 8181, 'relevance': 9, 'coherence': 8, 'fluency': 8}, {'id': 8182, 'relevance': 8, 'coherence': 4, 'fluency': 5}, {'id': 8183, 'relevance': 8, 'coherence': 6, 'fluency': 5}, {'id': 8184, 'relevance': 6, 'coherence': 5, 'fluency': 6}, {'id': 5099, 'relevance': 1, 'coherence': 2, 'fluency': 2}, {'id': 4526, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 4527, 'relevance': 1, 'coherence': 2, 'fluency': 1}, {'id': 4528, 'relevance': 1, 'coherence': 1, 'fluency': 2}, {'id': 4529, 'relevance': 2, 'coherence': 1, 'fluency': 2}, {'id': 4530, 'relevance': 1, 'coherence': 2, 'fluency': 2}, {'id': 5100, 'relevance': 10, 'coherence': 9, 'fluency': 9}, {'id': 3233, 'relevance': 7, 'coherence': 6, 'fluency': 6}, {'id': 3234, 'relevance': 7, 'coherence': 6, 'fluency': 6}, {'id': 3231, 'relevance': 5, 'coherence': 7, 'fluency': 5}, {'id': 3232, 'relevance': 8, 'coherence': 7, 'fluency': 8}, {'id': 3235, 'relevance': 10, 'coherence': 8, 'fluency': 7}, {'id': 3579, 'relevance': 4, 'coherence': 4, 'fluency': 3}, {'id': 3576, 'relevance': 10, 'coherence': 8, 'fluency': 8}, {'id': 3577, 'relevance': 4, 'coherence': 4, 'fluency': 9}, {'id': 3578, 'relevance': 8, 'coherence': 8, 'fluency': 9}, {'id': 5104, 'relevance': 4, 'coherence': 4, 'fluency': 6}, {'id': 3580, 'relevance': 5, 'coherence': 6, 'fluency': 6}, {'id': 1911, 'relevance': 3, 'coherence': 5, 'fluency': 1}, {'id': 1912, 'relevance': 5, 'coherence': 1, 'fluency': 3}, {'id': 1913, 'relevance': 3, 'coherence': 2, 'fluency': 2}, {'id': 1914, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 5106, 'relevance': 3, 'coherence': 3, 'fluency': 2}, {'id': 1915, 'relevance': 3, 'coherence': 3, 'fluency': 1}, {'id': 5111, 'relevance': 5, 'coherence': 6, 'fluency': 2}, {'id': 1743, 'relevance': 5, 'coherence': 6, 'fluency': 6}, {'id': 1741, 'relevance': 5, 'coherence': 6, 'fluency': 6}, {'id': 1742, 'relevance': 6, 'coherence': 4, 'fluency': 5}, {'id': 1744, 'relevance': 6, 'coherence': 5, 'fluency': 3}, {'id': 1745, 'relevance': 4, 'coherence': 5, 'fluency': 4}, {'id': 3467, 'relevance': 1, 'coherence': 2, 'fluency': 2}, {'id': 3466, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 3468, 'relevance': 1, 'coherence': 2, 'fluency': 1}, {'id': 3469, 'relevance': 1, 'coherence': 1, 'fluency': 1}, {'id': 3470, 'relevance': 2, 'coherence': 2, 'fluency': 1}, {'id': 5112, 'relevance': 2, 'coherence': 1, 'fluency': 1}, {'id': 5116, 'relevance': 4, 'coherence': 2, 'fluency': 2}, {'id': 4518, 'relevance': 0, 'coherence': 0, 'fluency': 0}, {'id': 4516, 'relevance': 3, 'coherence': 2, 'fluency': 2}, {'id': 4517, 'relevance': 1, 'coherence': 2, 'fluency': 2}, {'id': 4519, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 4520, 'relevance': 3, 'coherence': 4, 'fluency': 3}, {'id': 2436, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 5150, 'relevance': 8, 'coherence': 8, 'fluency': 9}, {'id': 2437, 'relevance': 9, 'coherence': 8, 'fluency': 9}, {'id': 2438, 'relevance': 8, 'coherence': 8, 'fluency': 7}, {'id': 2439, 'relevance': 8, 'coherence': 8, 'fluency': 9}, {'id': 2440, 'relevance': 8, 'coherence': 8, 'fluency': 9}, {'id': 3034, 'relevance': 8, 'coherence': 8, 'fluency': 7}, {'id': 3035, 'relevance': 7, 'coherence': 8, 'fluency': 6}, {'id': 5132, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 3032, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 3033, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 3031, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 825, 'relevance': 2, 'coherence': 2, 'fluency': 3}, {'id': 827, 'relevance': 5, 'coherence': 3, 'fluency': 3}, {'id': 828, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 829, 'relevance': 2, 'coherence': 2, 'fluency': 8}, {'id': 5175, 'relevance': 5, 'coherence': 3, 'fluency': 3}, {'id': 826, 'relevance': 2, 'coherence': 2, 'fluency': 3}, {'id': 3435, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 5146, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 3431, 'relevance': 5, 'coherence': 6, 'fluency': 7}, {'id': 3433, 'relevance': 4, 'coherence': 5, 'fluency': 6}, {'id': 3434, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 3432, 'relevance': 5, 'coherence': 6, 'fluency': 5}, {'id': 1332, 'relevance': 4, 'coherence': 5, 'fluency': 8}, {'id': 1333, 'relevance': 7, 'coherence': 9, 'fluency': 7}, {'id': 1331, 'relevance': 10, 'coherence': 7, 'fluency': 10}, {'id': 1334, 'relevance': 10, 'coherence': 10, 'fluency': 10}, {'id': 1335, 'relevance': 10, 'coherence': 7, 'fluency': 7}, {'id': 5151, 'relevance': 7, 'coherence': 10, 'fluency': 7}, {'id': 5148, 'relevance': 7, 'coherence': 7, 'fluency': 8}, {'id': 2612, 'relevance': 6, 'coherence': 9, 'fluency': 8}, {'id': 2615, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 2611, 'relevance': 8, 'coherence': 6, 'fluency': 6}, {'id': 2613, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 2614, 'relevance': 7, 'coherence': 7, 'fluency': 9}, {'id': 5192, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 4016, 'relevance': 6, 'coherence': 6, 'fluency': 7}, {'id': 4017, 'relevance': 7, 'coherence': 8, 'fluency': 5}, {'id': 4018, 'relevance': 6, 'coherence': 7, 'fluency': 6}, {'id': 4019, 'relevance': 7, 'coherence': 6, 'fluency': 7}, {'id': 4020, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 4025, 'relevance': 10, 'coherence': 10, 'fluency': 10}, {'id': 4021, 'relevance': 3, 'coherence': 3, 'fluency': 10}, {'id': 4022, 'relevance': 5, 'coherence': 5, 'fluency': 5}, {'id': 4023, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 4024, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 5154, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 1522, 'relevance': 3, 'coherence': 2, 'fluency': 3}, {'id': 5130, 'relevance': 2, 'coherence': 3, 'fluency': 3}, {'id': 1525, 'relevance': 4, 'coherence': 3, 'fluency': 3}, {'id': 1521, 'relevance': 3, 'coherence': 2, 'fluency': 4}, {'id': 1523, 'relevance': 2, 'coherence': 3, 'fluency': 2}, {'id': 1524, 'relevance': 3, 'coherence': 3, 'fluency': 4}, {'id': 2656, 'relevance': 3, 'coherence': 4, 'fluency': 4}, {'id': 2657, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 5138, 'relevance': 7, 'coherence': 7, 'fluency': 6}, {'id': 5139, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 5140, 'relevance': 7, 'coherence': 7, 'fluency': 6}, {'id': 2658, 'relevance': 3, 'coherence': 3, 'fluency': 4}, {'id': 2659, 'relevance': 3, 'coherence': 3, 'fluency': 4}, {'id': 2660, 'relevance': 5, 'coherence': 5, 'fluency': 5}, {'id': 3656, 'relevance': 0, 'coherence': 0, 'fluency': 0}, {'id': 3657, 'relevance': 0, 'coherence': 0, 'fluency': 0}, {'id': 3658, 'relevance': 0, 'coherence': 0, 'fluency': 0}, {'id': 3659, 'relevance': 0, 'coherence': 0, 'fluency': 0}, {'id': 3660, 'relevance': 0, 'coherence': 0, 'fluency': 0}, {'id': 5217, 'relevance': 0, 'coherence': 0, 'fluency': 0}, {'id': 8366, 'relevance': 7, 'coherence': 3, 'fluency': 2}, {'id': 8365, 'relevance': 3, 'coherence': 3, 'fluency': 7}, {'id': 8367, 'relevance': 7, 'coherence': 3, 'fluency': 7}, {'id': 8368, 'relevance': 7, 'coherence': 3, 'fluency': 7}, {'id': 8369, 'relevance': 7, 'coherence': 7, 'fluency': 3}, {'id': 16124, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 8371, 'relevance': 6, 'coherence': 8, 'fluency': 8}, {'id': 8372, 'relevance': 5, 'coherence': 7, 'fluency': 7}, {'id': 8370, 'relevance': 4, 'coherence': 6, 'fluency': 7}, {'id': 8373, 'relevance': 6, 'coherence': 6, 'fluency': 8}, {'id': 18561, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 8374, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 8480, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 8481, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 8482, 'relevance': 8, 'coherence': 7, 'fluency': 8}, {'id': 8483, 'relevance': 8, 'coherence': 7, 'fluency': 8}, {'id': 15674, 'relevance': 9, 'coherence': 8, 'fluency': 9}, {'id': 8484, 'relevance': 10, 'coherence': 10, 'fluency': 10}, {'id': 8540, 'relevance': 4, 'coherence': 4, 'fluency': 3}, {'id': 8541, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 8542, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 8543, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 8544, 'relevance': 4, 'coherence': 4, 'fluency': 3}, {'id': 18328, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 8485, 'relevance': 3, 'coherence': 6, 'fluency': 6}, {'id': 8486, 'relevance': 3, 'coherence': 6, 'fluency': 6}, {'id': 15736, 'relevance': 9, 'coherence': 3, 'fluency': 9}, {'id': 8487, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 8488, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 8489, 'relevance': 6, 'coherence': 3, 'fluency': 3}, {'id': 8610, 'relevance': 8, 'coherence': 7, 'fluency': 8}, {'id': 8611, 'relevance': 7, 'coherence': 8, 'fluency': 10}, {'id': 16130, 'relevance': 7, 'coherence': 8, 'fluency': 8}, {'id': 8612, 'relevance': 9, 'coherence': 7, 'fluency': 8}, {'id': 8613, 'relevance': 8, 'coherence': 8, 'fluency': 9}, {'id': 8614, 'relevance': 8, 'coherence': 8, 'fluency': 10}, {'id': 8615, 'relevance': 9, 'coherence': 6, 'fluency': 3}, {'id': 8616, 'relevance': 3, 'coherence': 6, 'fluency': 3}, {'id': 8617, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 8618, 'relevance': 6, 'coherence': 6, 'fluency': 3}, {'id': 8619, 'relevance': 6, 'coherence': 6, 'fluency': 3}, {'id': 16210, 'relevance': 6, 'coherence': 6, 'fluency': 3}, {'id': 8979, 'relevance': 0, 'coherence': 0, 'fluency': 0}, {'id': 15620, 'relevance': 0, 'coherence': 0, 'fluency': 0}, {'id': 8975, 'relevance': 0, 'coherence': 0, 'fluency': 0}, {'id': 8976, 'relevance': 0, 'coherence': 0, 'fluency': 0}, {'id': 8977, 'relevance': 0, 'coherence': 0, 'fluency': 0}, {'id': 8978, 'relevance': 0, 'coherence': 0, 'fluency': 0}, {'id': 9250, 'relevance': 2, 'coherence': 2, 'fluency': 4}, {'id': 9251, 'relevance': 5, 'coherence': 3, 'fluency': 4}, {'id': 9252, 'relevance': 3, 'coherence': 3, 'fluency': 2}, {'id': 9253, 'relevance': 3, 'coherence': 3, 'fluency': 2}, {'id': 9254, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 15907, 'relevance': 2, 'coherence': 3, 'fluency': 2}, {'id': 9300, 'relevance': 10, 'coherence': 9, 'fluency': 9}, {'id': 9301, 'relevance': 8, 'coherence': 7, 'fluency': 7}, {'id': 9302, 'relevance': 5, 'coherence': 4, 'fluency': 6}, {'id': 9303, 'relevance': 4, 'coherence': 4, 'fluency': 6}, {'id': 18458, 'relevance': 7, 'coherence': 6, 'fluency': 7}, {'id': 9304, 'relevance': 4, 'coherence': 4, 'fluency': 6}, {'id': 9590, 'relevance': 5, 'coherence': 5, 'fluency': 5}, {'id': 9591, 'relevance': 7, 'coherence': 5, 'fluency': 4}, {'id': 9592, 'relevance': 8, 'coherence': 6, 'fluency': 5}, {'id': 9593, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 9594, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 16172, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 18276, 'relevance': 4, 'coherence': 4, 'fluency': 5}, {'id': 9475, 'relevance': 7, 'coherence': 8, 'fluency': 9}, {'id': 9476, 'relevance': 8, 'coherence': 7, 'fluency': 8}, {'id': 9477, 'relevance': 8, 'coherence': 10, 'fluency': 8}, {'id': 9478, 'relevance': 8, 'coherence': 7, 'fluency': 8}, {'id': 9479, 'relevance': 7, 'coherence': 7, 'fluency': 8}, {'id': 9649, 'relevance': 5, 'coherence': 4, 'fluency': 3}, {'id': 9645, 'relevance': 6, 'coherence': 7, 'fluency': 7}, {'id': 9646, 'relevance': 8, 'coherence': 6, 'fluency': 6}, {'id': 9647, 'relevance': 10, 'coherence': 9, 'fluency': 8}, {'id': 9648, 'relevance': 10, 'coherence': 10, 'fluency': 10}, {'id': 15705, 'relevance': 7, 'coherence': 7, 'fluency': 6}, {'id': 9850, 'relevance': 4, 'coherence': 5, 'fluency': 4}, {'id': 9854, 'relevance': 4, 'coherence': 3, 'fluency': 4}, {'id': 9853, 'relevance': 4, 'coherence': 5, 'fluency': 2}, {'id': 15970, 'relevance': 4, 'coherence': 5, 'fluency': 5}, {'id': 9851, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 9852, 'relevance': 4, 'coherence': 3, 'fluency': 5}, {'id': 15978, 'relevance': 9, 'coherence': 9, 'fluency': 8}, {'id': 9767, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 9768, 'relevance': 10, 'coherence': 9, 'fluency': 9}, {'id': 9769, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 9765, 'relevance': 9, 'coherence': 10, 'fluency': 9}, {'id': 9766, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 9732, 'relevance': 3, 'coherence': 3, 'fluency': 2}, {'id': 9733, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 9734, 'relevance': 5, 'coherence': 5, 'fluency': 5}, {'id': 16243, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 9730, 'relevance': 3, 'coherence': 2, 'fluency': 3}, {'id': 9731, 'relevance': 3, 'coherence': 2, 'fluency': 3}, {'id': 9860, 'relevance': 7, 'coherence': 6, 'fluency': 7}, {'id': 9861, 'relevance': 7, 'coherence': 7, 'fluency': 6}, {'id': 9862, 'relevance': 7, 'coherence': 7, 'fluency': 9}, {'id': 9863, 'relevance': 9, 'coherence': 7, 'fluency': 9}, {'id': 9864, 'relevance': 10, 'coherence': 9, 'fluency': 9}, {'id': 18435, 'relevance': 9, 'coherence': 7, 'fluency': 7}, {'id': 9780, 'relevance': 3, 'coherence': 7, 'fluency': 7}, {'id': 9781, 'relevance': 3, 'coherence': 7, 'fluency': 8}, {'id': 9782, 'relevance': 6, 'coherence': 7, 'fluency': 7}, {'id': 9783, 'relevance': 4, 'coherence': 7, 'fluency': 6}, {'id': 9784, 'relevance': 7, 'coherence': 7, 'fluency': 3}, {'id': 18592, 'relevance': 3, 'coherence': 7, 'fluency': 6}, {'id': 10022, 'relevance': 8, 'coherence': 8, 'fluency': 6}, {'id': 10023, 'relevance': 8, 'coherence': 6, 'fluency': 6}, {'id': 10024, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 10020, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 10021, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 15739, 'relevance': 6, 'coherence': 4, 'fluency': 4}, {'id': 9965, 'relevance': 8, 'coherence': 7, 'fluency': 8}, {'id': 9966, 'relevance': 8, 'coherence': 7, 'fluency': 7}, {'id': 9967, 'relevance': 8, 'coherence': 6, 'fluency': 8}, {'id': 9969, 'relevance': 7, 'coherence': 8, 'fluency': 8}, {'id': 18302, 'relevance': 7, 'coherence': 8, 'fluency': 8}, {'id': 9968, 'relevance': 6, 'coherence': 8, 'fluency': 8}, {'id': 15802, 'relevance': 4, 'coherence': 2, 'fluency': 3}, {'id': 7951, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 7954, 'relevance': 7, 'coherence': 5, 'fluency': 4}, {'id': 7950, 'relevance': 4, 'coherence': 3, 'fluency': 4}, {'id': 7952, 'relevance': 4, 'coherence': 3, 'fluency': 4}, {'id': 7953, 'relevance': 5, 'coherence': 7, 'fluency': 5}, {'id': 7527, 'relevance': 5, 'coherence': 4, 'fluency': 3}, {'id': 7526, 'relevance': 2, 'coherence': 4, 'fluency': 2}, {'id': 7525, 'relevance': 4, 'coherence': 5, 'fluency': 6}, {'id': 15824, 'relevance': 4, 'coherence': 3, 'fluency': 8}, {'id': 7528, 'relevance': 4, 'coherence': 5, 'fluency': 6}, {'id': 7529, 'relevance': 3, 'coherence': 5, 'fluency': 3}, {'id': 6026, 'relevance': 8, 'coherence': 7, 'fluency': 7}, {'id': 6027, 'relevance': 8, 'coherence': 7, 'fluency': 7}, {'id': 6028, 'relevance': 7, 'coherence': 8, 'fluency': 7}, {'id': 6029, 'relevance': 8, 'coherence': 6, 'fluency': 7}, {'id': 15846, 'relevance': 8, 'coherence': 8, 'fluency': 7}, {'id': 6025, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 8621, 'relevance': 1, 'coherence': 2, 'fluency': 2}, {'id': 8622, 'relevance': 4, 'coherence': 3, 'fluency': 3}, {'id': 8623, 'relevance': 1, 'coherence': 1, 'fluency': 2}, {'id': 15875, 'relevance': 1, 'coherence': 1, 'fluency': 1}, {'id': 8620, 'relevance': 2, 'coherence': 3, 'fluency': 2}, {'id': 8624, 'relevance': 2, 'coherence': 3, 'fluency': 3}, {'id': 16101, 'relevance': 2, 'coherence': 3, 'fluency': 1}, {'id': 6240, 'relevance': 1, 'coherence': 2, 'fluency': 2}, {'id': 6241, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 6242, 'relevance': 2, 'coherence': 3, 'fluency': 2}, {'id': 6243, 'relevance': 2, 'coherence': 2, 'fluency': 3}, {'id': 6244, 'relevance': 3, 'coherence': 3, 'fluency': 2}, {'id': 18425, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 8625, 'relevance': 2, 'coherence': 3, 'fluency': 2}, {'id': 8626, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 8627, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 8628, 'relevance': 1, 'coherence': 2, 'fluency': 3}, {'id': 8629, 'relevance': 3, 'coherence': 2, 'fluency': 1}, {'id': 10416, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 10417, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 10419, 'relevance': 9, 'coherence': 9, 'fluency': 3}, {'id': 10420, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 10418, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 18596, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 10616, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 10617, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 10618, 'relevance': 10, 'coherence': 10, 'fluency': 3}, {'id': 10619, 'relevance': 3, 'coherence': 10, 'fluency': 3}, {'id': 10620, 'relevance': 10, 'coherence': 10, 'fluency': 3}, {'id': 15749, 'relevance': 3, 'coherence': 3, 'fluency': 10}, {'id': 10551, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 10552, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 16190, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 10553, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 10554, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 10555, 'relevance': 4, 'coherence': 2, 'fluency': 2}, {'id': 10491, 'relevance': 9, 'coherence': 8, 'fluency': 9}, {'id': 10492, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 10493, 'relevance': 8, 'coherence': 7, 'fluency': 8}, {'id': 10494, 'relevance': 6, 'coherence': 7, 'fluency': 7}, {'id': 10495, 'relevance': 8, 'coherence': 7, 'fluency': 8}, {'id': 16227, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 15883, 'relevance': 3, 'coherence': 1, 'fluency': 3}, {'id': 10956, 'relevance': 2, 'coherence': 1, 'fluency': 2}, {'id': 10957, 'relevance': 2, 'coherence': 2, 'fluency': 1}, {'id': 10958, 'relevance': 2, 'coherence': 1, 'fluency': 2}, {'id': 10959, 'relevance': 1, 'coherence': 1, 'fluency': 1}, {'id': 10960, 'relevance': 1, 'coherence': 1, 'fluency': 1}, {'id': 10906, 'relevance': 8, 'coherence': 8, 'fluency': 7}, {'id': 10907, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 10908, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 10909, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 10910, 'relevance': 8, 'coherence': 8, 'fluency': 9}, {'id': 18749, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 10901, 'relevance': 8, 'coherence': 7, 'fluency': 7}, {'id': 10902, 'relevance': 8, 'coherence': 6, 'fluency': 8}, {'id': 10903, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 10904, 'relevance': 8, 'coherence': 7, 'fluency': 7}, {'id': 10905, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 18809, 'relevance': 7, 'coherence': 8, 'fluency': 7}, {'id': 11038, 'relevance': 8, 'coherence': 7, 'fluency': 8}, {'id': 11039, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 11040, 'relevance': 8, 'coherence': 7, 'fluency': 6}, {'id': 11036, 'relevance': 4, 'coherence': 5, 'fluency': 4}, {'id': 11037, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 15926, 'relevance': 8, 'coherence': 7, 'fluency': 7}, {'id': 11096, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 11097, 'relevance': 10, 'coherence': 9, 'fluency': 10}, {'id': 16060, 'relevance': 10, 'coherence': 9, 'fluency': 9}, {'id': 11098, 'relevance': 5, 'coherence': 6, 'fluency': 6}, {'id': 11099, 'relevance': 9, 'coherence': 7, 'fluency': 7}, {'id': 11100, 'relevance': 9, 'coherence': 8, 'fluency': 8}, {'id': 16189, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 11104, 'relevance': 8, 'coherence': 5, 'fluency': 6}, {'id': 11105, 'relevance': 8, 'coherence': 6, 'fluency': 6}, {'id': 11101, 'relevance': 6, 'coherence': 5, 'fluency': 5}, {'id': 11102, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 11103, 'relevance': 8, 'coherence': 5, 'fluency': 6}, {'id': 11268, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 11266, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 11267, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 18366, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 11269, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 11270, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 11551, 'relevance': 3, 'coherence': 2, 'fluency': 1}, {'id': 16246, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 11552, 'relevance': 3, 'coherence': 2, 'fluency': 2}, {'id': 11553, 'relevance': 1, 'coherence': 1, 'fluency': 1}, {'id': 11554, 'relevance': 2, 'coherence': 1, 'fluency': 1}, {'id': 11555, 'relevance': 3, 'coherence': 3, 'fluency': 2}, {'id': 11316, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 11318, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 11320, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 18307, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 11317, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 11319, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 11531, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 11532, 'relevance': 3, 'coherence': 3, 'fluency': 7}, {'id': 11533, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 11534, 'relevance': 8, 'coherence': 3, 'fluency': 8}, {'id': 11535, 'relevance': 3, 'coherence': 8, 'fluency': 3}, {'id': 18755, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 15968, 'relevance': 3, 'coherence': 1, 'fluency': 2}, {'id': 11536, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 11537, 'relevance': 2, 'coherence': 3, 'fluency': 2}, {'id': 11538, 'relevance': 3, 'coherence': 2, 'fluency': 2}, {'id': 11539, 'relevance': 2, 'coherence': 2, 'fluency': 1}, {'id': 11540, 'relevance': 1, 'coherence': 2, 'fluency': 2}, {'id': 11546, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 11547, 'relevance': 1, 'coherence': 1, 'fluency': 1}, {'id': 11548, 'relevance': 3, 'coherence': 3, 'fluency': 2}, {'id': 11549, 'relevance': 2, 'coherence': 4, 'fluency': 3}, {'id': 11550, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 16038, 'relevance': 3, 'coherence': 2, 'fluency': 2}, {'id': 15843, 'relevance': 6, 'coherence': 7, 'fluency': 7}, {'id': 11485, 'relevance': 5, 'coherence': 5, 'fluency': 5}, {'id': 11481, 'relevance': 5, 'coherence': 6, 'fluency': 8}, {'id': 11482, 'relevance': 5, 'coherence': 6, 'fluency': 6}, {'id': 11483, 'relevance': 5, 'coherence': 6, 'fluency': 5}, {'id': 11484, 'relevance': 5, 'coherence': 5, 'fluency': 6}, {'id': 11571, 'relevance': 8, 'coherence': 5, 'fluency': 9}, {'id': 11572, 'relevance': 2, 'coherence': 2, 'fluency': 8}, {'id': 11573, 'relevance': 3, 'coherence': 3, 'fluency': 6}, {'id': 11574, 'relevance': 5, 'coherence': 4, 'fluency': 9}, {'id': 15750, 'relevance': 4, 'coherence': 5, 'fluency': 4}, {'id': 11575, 'relevance': 7, 'coherence': 7, 'fluency': 8}, {'id': 11596, 'relevance': 3, 'coherence': 6, 'fluency': 6}, {'id': 11597, 'relevance': 6, 'coherence': 6, 'fluency': 3}, {'id': 11598, 'relevance': 3, 'coherence': 6, 'fluency': 3}, {'id': 11599, 'relevance': 3, 'coherence': 6, 'fluency': 6}, {'id': 11600, 'relevance': 3, 'coherence': 6, 'fluency': 6}, {'id': 18703, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 11671, 'relevance': 7, 'coherence': 6, 'fluency': 6}, {'id': 11672, 'relevance': 7, 'coherence': 8, 'fluency': 7}, {'id': 11673, 'relevance': 6, 'coherence': 6, 'fluency': 7}, {'id': 11674, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 11675, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 18303, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 11569, 'relevance': 2, 'coherence': 4, 'fluency': 8}, {'id': 11566, 'relevance': 6, 'coherence': 9, 'fluency': 6}, {'id': 11567, 'relevance': 9, 'coherence': 4, 'fluency': 4}, {'id': 11568, 'relevance': 9, 'coherence': 6, 'fluency': 8}, {'id': 11570, 'relevance': 8, 'coherence': 5, 'fluency': 5}, {'id': 18414, 'relevance': 2, 'coherence': 5, 'fluency': 8}, {'id': 11601, 'relevance': 1, 'coherence': 2, 'fluency': 1}, {'id': 11602, 'relevance': 3, 'coherence': 1, 'fluency': 1}, {'id': 11603, 'relevance': 2, 'coherence': 1, 'fluency': 1}, {'id': 11604, 'relevance': 1, 'coherence': 3, 'fluency': 1}, {'id': 11605, 'relevance': 2, 'coherence': 1, 'fluency': 3}, {'id': 18636, 'relevance': 2, 'coherence': 1, 'fluency': 2}, {'id': 11606, 'relevance': 3, 'coherence': 4, 'fluency': 3}, {'id': 11607, 'relevance': 3, 'coherence': 3, 'fluency': 2}, {'id': 11608, 'relevance': 3, 'coherence': 3, 'fluency': 1}, {'id': 11609, 'relevance': 3, 'coherence': 3, 'fluency': 2}, {'id': 11610, 'relevance': 3, 'coherence': 2, 'fluency': 2}, {'id': 18728, 'relevance': 2, 'coherence': 3, 'fluency': 3}, {'id': 11830, 'relevance': 7, 'coherence': 8, 'fluency': 8}, {'id': 11826, 'relevance': 7, 'coherence': 8, 'fluency': 8}, {'id': 11827, 'relevance': 7, 'coherence': 6, 'fluency': 8}, {'id': 11828, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 11829, 'relevance': 7, 'coherence': 6, 'fluency': 8}, {'id': 18832, 'relevance': 7, 'coherence': 7, 'fluency': 8}, {'id': 12061, 'relevance': 5, 'coherence': 5, 'fluency': 5}, {'id': 12062, 'relevance': 5, 'coherence': 5, 'fluency': 5}, {'id': 12063, 'relevance': 5, 'coherence': 5, 'fluency': 5}, {'id': 12065, 'relevance': 5, 'coherence': 5, 'fluency': 5}, {'id': 18680, 'relevance': 5, 'coherence': 5, 'fluency': 5}, {'id': 12064, 'relevance': 5, 'coherence': 5, 'fluency': 5}, {'id': 15919, 'relevance': 7, 'coherence': 7, 'fluency': 3}, {'id': 12202, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 12203, 'relevance': 3, 'coherence': 5, 'fluency': 3}, {'id': 12204, 'relevance': 3, 'coherence': 5, 'fluency': 5}, {'id': 12205, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 12201, 'relevance': 3, 'coherence': 3, 'fluency': 5}, {'id': 15692, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 12143, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 12145, 'relevance': 5, 'coherence': 5, 'fluency': 5}, {'id': 12144, 'relevance': 9, 'coherence': 10, 'fluency': 10}, {'id': 12141, 'relevance': 9, 'coherence': 10, 'fluency': 10}, {'id': 12142, 'relevance': 5, 'coherence': 5, 'fluency': 5}, {'id': 12226, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 12227, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 12228, 'relevance': 5, 'coherence': 5, 'fluency': 4}, {'id': 12229, 'relevance': 4, 'coherence': 4, 'fluency': 5}, {'id': 12230, 'relevance': 5, 'coherence': 6, 'fluency': 6}, {'id': 16063, 'relevance': 5, 'coherence': 5, 'fluency': 6}, {'id': 12087, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 12088, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 12089, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 12090, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 18746, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 12086, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 8076, 'relevance': 3, 'coherence': 3, 'fluency': 9}, {'id': 12318, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 8075, 'relevance': 3, 'coherence': 3, 'fluency': 9}, {'id': 8077, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 8078, 'relevance': 6, 'coherence': 6, 'fluency': 9}, {'id': 8079, 'relevance': 6, 'coherence': 6, 'fluency': 3}, {'id': 11530, 'relevance': 5, 'coherence': 3, 'fluency': 5}, {'id': 11526, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 11527, 'relevance': 3, 'coherence': 3, 'fluency': 4}, {'id': 11528, 'relevance': 4, 'coherence': 3, 'fluency': 3}, {'id': 11529, 'relevance': 4, 'coherence': 3, 'fluency': 3}, {'id': 12323, 'relevance': 6, 'coherence': 4, 'fluency': 4}, {'id': 7943, 'relevance': 0, 'coherence': 0, 'fluency': 0}, {'id': 7941, 'relevance': 2, 'coherence': 3, 'fluency': 2}, {'id': 7942, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 7944, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 15532, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 7940, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 12347, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 12348, 'relevance': 2, 'coherence': 2, 'fluency': 1}, {'id': 12349, 'relevance': 1, 'coherence': 2, 'fluency': 1}, {'id': 12350, 'relevance': 2, 'coherence': 1, 'fluency': 2}, {'id': 12351, 'relevance': 2, 'coherence': 1, 'fluency': 1}, {'id': 15708, 'relevance': 1, 'coherence': 2, 'fluency': 1}, {'id': 12486, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 12483, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 15744, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 12482, 'relevance': 6, 'coherence': 6, 'fluency': 3}, {'id': 12484, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 12485, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 15751, 'relevance': 10, 'coherence': 10, 'fluency': 10}, {'id': 12527, 'relevance': 6, 'coherence': 2, 'fluency': 2}, {'id': 12528, 'relevance': 6, 'coherence': 2, 'fluency': 6}, {'id': 12529, 'relevance': 6, 'coherence': 2, 'fluency': 2}, {'id': 12530, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 12531, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 12407, 'relevance': 6, 'coherence': 7, 'fluency': 7}, {'id': 12408, 'relevance': 6, 'coherence': 6, 'fluency': 7}, {'id': 12409, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 12410, 'relevance': 6, 'coherence': 7, 'fluency': 6}, {'id': 12411, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 18504, 'relevance': 7, 'coherence': 6, 'fluency': 7}, {'id': 12516, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 16056, 'relevance': 8, 'coherence': 7, 'fluency': 8}, {'id': 12512, 'relevance': 4, 'coherence': 4, 'fluency': 6}, {'id': 12513, 'relevance': 4, 'coherence': 5, 'fluency': 6}, {'id': 12514, 'relevance': 4, 'coherence': 4, 'fluency': 5}, {'id': 12515, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 12722, 'relevance': 10, 'coherence': 10, 'fluency': 10}, {'id': 12723, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 12724, 'relevance': 5, 'coherence': 3, 'fluency': 5}, {'id': 12725, 'relevance': 10, 'coherence': 10, 'fluency': 10}, {'id': 12726, 'relevance': 10, 'coherence': 10, 'fluency': 10}, {'id': 15771, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 15965, 'relevance': 6, 'coherence': 5, 'fluency': 6}, {'id': 12670, 'relevance': 10, 'coherence': 10, 'fluency': 8}, {'id': 12671, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 12667, 'relevance': 9, 'coherence': 8, 'fluency': 7}, {'id': 12668, 'relevance': 6, 'coherence': 5, 'fluency': 5}, {'id': 12669, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 12557, 'relevance': 3, 'coherence': 6, 'fluency': 6}, {'id': 12558, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 12559, 'relevance': 9, 'coherence': 9, 'fluency': 3}, {'id': 12560, 'relevance': 6, 'coherence': 9, 'fluency': 9}, {'id': 12561, 'relevance': 3, 'coherence': 9, 'fluency': 3}, {'id': 15972, 'relevance': 3, 'coherence': 6, 'fluency': 3}, {'id': 12687, 'relevance': 0, 'coherence': 0, 'fluency': 0}, {'id': 12688, 'relevance': 0, 'coherence': 0, 'fluency': 0}, {'id': 12689, 'relevance': 0, 'coherence': 0, 'fluency': 0}, {'id': 12690, 'relevance': 0, 'coherence': 0, 'fluency': 0}, {'id': 12691, 'relevance': 0, 'coherence': 0, 'fluency': 0}, {'id': 18361, 'relevance': 0, 'coherence': 0, 'fluency': 0}, {'id': 12651, 'relevance': 9, 'coherence': 7, 'fluency': 8}, {'id': 12647, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 12648, 'relevance': 8, 'coherence': 8, 'fluency': 6}, {'id': 12649, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 12650, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 18437, 'relevance': 8, 'coherence': 8, 'fluency': 7}, {'id': 12646, 'relevance': 3, 'coherence': 4, 'fluency': 4}, {'id': 18512, 'relevance': 6, 'coherence': 6, 'fluency': 7}, {'id': 12642, 'relevance': 8, 'coherence': 7, 'fluency': 8}, {'id': 12643, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 12644, 'relevance': 7, 'coherence': 7, 'fluency': 8}, {'id': 12645, 'relevance': 6, 'coherence': 7, 'fluency': 7}, {'id': 12603, 'relevance': 4, 'coherence': 4, 'fluency': 6}, {'id': 12602, 'relevance': 2, 'coherence': 3, 'fluency': 4}, {'id': 12604, 'relevance': 2, 'coherence': 2, 'fluency': 4}, {'id': 12605, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 12606, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 18826, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 18644, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 12596, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 12595, 'relevance': 8, 'coherence': 7, 'fluency': 8}, {'id': 12592, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 12593, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 12594, 'relevance': 8, 'coherence': 9, 'fluency': 8}, {'id': 18716, 'relevance': 6, 'coherence': 7, 'fluency': 9}, {'id': 12627, 'relevance': 2, 'coherence': 10, 'fluency': 3}, {'id': 12628, 'relevance': 10, 'coherence': 2, 'fluency': 3}, {'id': 12629, 'relevance': 3, 'coherence': 2, 'fluency': 10}, {'id': 12630, 'relevance': 3, 'coherence': 9, 'fluency': 3}, {'id': 12631, 'relevance': 3, 'coherence': 2, 'fluency': 3}, {'id': 16035, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 12887, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 12888, 'relevance': 8, 'coherence': 8, 'fluency': 9}, {'id': 12889, 'relevance': 6, 'coherence': 6, 'fluency': 9}, {'id': 12890, 'relevance': 9, 'coherence': 10, 'fluency': 10}, {'id': 12891, 'relevance': 7, 'coherence': 7, 'fluency': 8}, {'id': 13039, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 13040, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 13041, 'relevance': 10, 'coherence': 9, 'fluency': 10}, {'id': 15608, 'relevance': 8, 'coherence': 8, 'fluency': 7}, {'id': 13037, 'relevance': 7, 'coherence': 8, 'fluency': 8}, {'id': 13038, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 12939, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 16118, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 12937, 'relevance': 5, 'coherence': 6, 'fluency': 5}, {'id': 12938, 'relevance': 4, 'coherence': 4, 'fluency': 5}, {'id': 12940, 'relevance': 5, 'coherence': 4, 'fluency': 5}, {'id': 12941, 'relevance': 5, 'coherence': 6, 'fluency': 5}, {'id': 13198, 'relevance': 1, 'coherence': 1, 'fluency': 1}, {'id': 13197, 'relevance': 3, 'coherence': 3, 'fluency': 4}, {'id': 13199, 'relevance': 3, 'coherence': 3, 'fluency': 4}, {'id': 13200, 'relevance': 3, 'coherence': 2, 'fluency': 2}, {'id': 16027, 'relevance': 2, 'coherence': 1, 'fluency': 1}, {'id': 13201, 'relevance': 2, 'coherence': 3, 'fluency': 3}, {'id': 15831, 'relevance': 7, 'coherence': 7, 'fluency': 9}, {'id': 13174, 'relevance': 6, 'coherence': 6, 'fluency': 8}, {'id': 13175, 'relevance': 9, 'coherence': 6, 'fluency': 8}, {'id': 13176, 'relevance': 7, 'coherence': 7, 'fluency': 8}, {'id': 13172, 'relevance': 8, 'coherence': 8, 'fluency': 9}, {'id': 13173, 'relevance': 7, 'coherence': 7, 'fluency': 10}, {'id': 13228, 'relevance': 3, 'coherence': 8, 'fluency': 10}, {'id': 13227, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 13229, 'relevance': 2, 'coherence': 9, 'fluency': 2}, {'id': 13230, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 13231, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 15670, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 13237, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 15954, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 13238, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 13239, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 13240, 'relevance': 8, 'coherence': 7, 'fluency': 7}, {'id': 13241, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 15997, 'relevance': 8, 'coherence': 6, 'fluency': 4}, {'id': 13276, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 13272, 'relevance': 8, 'coherence': 8, 'fluency': 10}, {'id': 13273, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 13274, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 13275, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 13202, 'relevance': 5, 'coherence': 3, 'fluency': 5}, {'id': 13203, 'relevance': 4, 'coherence': 3, 'fluency': 4}, {'id': 13204, 'relevance': 4, 'coherence': 5, 'fluency': 4}, {'id': 13205, 'relevance': 4, 'coherence': 5, 'fluency': 4}, {'id': 13206, 'relevance': 3, 'coherence': 4, 'fluency': 4}, {'id': 16217, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 13224, 'relevance': 7, 'coherence': 6, 'fluency': 6}, {'id': 13225, 'relevance': 9, 'coherence': 7, 'fluency': 8}, {'id': 13226, 'relevance': 8, 'coherence': 7, 'fluency': 7}, {'id': 16003, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 13222, 'relevance': 8, 'coherence': 6, 'fluency': 7}, {'id': 13223, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 13517, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 16170, 'relevance': 4, 'coherence': 3, 'fluency': 3}, {'id': 13518, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 13520, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 13521, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 13519, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 16009, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 13588, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 13587, 'relevance': 10, 'coherence': 10, 'fluency': 10}, {'id': 13589, 'relevance': 9, 'coherence': 8, 'fluency': 8}, {'id': 13590, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 13591, 'relevance': 8, 'coherence': 4, 'fluency': 5}, {'id': 13542, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 13543, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 18335, 'relevance': 6, 'coherence': 2, 'fluency': 7}, {'id': 13544, 'relevance': 8, 'coherence': 8, 'fluency': 7}, {'id': 13545, 'relevance': 9, 'coherence': 9, 'fluency': 10}, {'id': 13546, 'relevance': 6, 'coherence': 5, 'fluency': 7}, {'id': 18432, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 13586, 'relevance': 10, 'coherence': 8, 'fluency': 10}, {'id': 13582, 'relevance': 10, 'coherence': 10, 'fluency': 10}, {'id': 13583, 'relevance': 6, 'coherence': 4, 'fluency': 8}, {'id': 13584, 'relevance': 8, 'coherence': 4, 'fluency': 8}, {'id': 13585, 'relevance': 10, 'coherence': 10, 'fluency': 10}, {'id': 13712, 'relevance': 4, 'coherence': 10, 'fluency': 10}, {'id': 13714, 'relevance': 7, 'coherence': 9, 'fluency': 2}, {'id': 13715, 'relevance': 2, 'coherence': 10, 'fluency': 8}, {'id': 15854, 'relevance': 6, 'coherence': 5, 'fluency': 10}, {'id': 13713, 'relevance': 10, 'coherence': 3, 'fluency': 10}, {'id': 13716, 'relevance': 9, 'coherence': 6, 'fluency': 10}, {'id': 13697, 'relevance': 3, 'coherence': 3, 'fluency': 6}, {'id': 13698, 'relevance': 3, 'coherence': 3, 'fluency': 4}, {'id': 13699, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 13700, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 13701, 'relevance': 4, 'coherence': 2, 'fluency': 3}, {'id': 15611, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 13722, 'relevance': 1, 'coherence': 1, 'fluency': 2}, {'id': 13723, 'relevance': 3, 'coherence': 3, 'fluency': 1}, {'id': 13724, 'relevance': 2, 'coherence': 2, 'fluency': 1}, {'id': 18326, 'relevance': 1, 'coherence': 1, 'fluency': 1}, {'id': 13725, 'relevance': 2, 'coherence': 2, 'fluency': 1}, {'id': 13726, 'relevance': 1, 'coherence': 1, 'fluency': 2}, {'id': 15718, 'relevance': 4, 'coherence': 3, 'fluency': 5}, {'id': 13707, 'relevance': 4, 'coherence': 3, 'fluency': 3}, {'id': 13708, 'relevance': 2, 'coherence': 3, 'fluency': 2}, {'id': 13709, 'relevance': 1, 'coherence': 2, 'fluency': 2}, {'id': 13710, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 13711, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 13706, 'relevance': 3, 'coherence': 4, 'fluency': 4}, {'id': 13702, 'relevance': 10, 'coherence': 8, 'fluency': 8}, {'id': 13703, 'relevance': 6, 'coherence': 8, 'fluency': 8}, {'id': 13704, 'relevance': 6, 'coherence': 8, 'fluency': 8}, {'id': 13705, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 15625, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 13766, 'relevance': 3, 'coherence': 3, 'fluency': 1}, {'id': 15897, 'relevance': 1, 'coherence': 2, 'fluency': 2}, {'id': 13762, 'relevance': 3, 'coherence': 2, 'fluency': 1}, {'id': 13763, 'relevance': 1, 'coherence': 3, 'fluency': 1}, {'id': 13764, 'relevance': 2, 'coherence': 2, 'fluency': 1}, {'id': 13765, 'relevance': 1, 'coherence': 3, 'fluency': 1}, {'id': 14193, 'relevance': 9, 'coherence': 8, 'fluency': 8}, {'id': 14194, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 14195, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 14196, 'relevance': 7, 'coherence': 8, 'fluency': 8}, {'id': 16222, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 14192, 'relevance': 6, 'coherence': 7, 'fluency': 7}, {'id': 14187, 'relevance': 2, 'coherence': 3, 'fluency': 9}, {'id': 14188, 'relevance': 3, 'coherence': 3, 'fluency': 8}, {'id': 14189, 'relevance': 2, 'coherence': 3, 'fluency': 7}, {'id': 15755, 'relevance': 2, 'coherence': 2, 'fluency': 10}, {'id': 14190, 'relevance': 2, 'coherence': 3, 'fluency': 9}, {'id': 14191, 'relevance': 2, 'coherence': 2, 'fluency': 9}, {'id': 14166, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 14165, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 14162, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 14163, 'relevance': 8, 'coherence': 7, 'fluency': 8}, {'id': 14164, 'relevance': 8, 'coherence': 7, 'fluency': 8}, {'id': 18489, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 14147, 'relevance': 1, 'coherence': 2, 'fluency': 4}, {'id': 14148, 'relevance': 1, 'coherence': 3, 'fluency': 4}, {'id': 14149, 'relevance': 3, 'coherence': 4, 'fluency': 5}, {'id': 14150, 'relevance': 4, 'coherence': 2, 'fluency': 3}, {'id': 14151, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 18572, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 14327, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 14328, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 14329, 'relevance': 4, 'coherence': 5, 'fluency': 4}, {'id': 14330, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 16196, 'relevance': 4, 'coherence': 5, 'fluency': 4}, {'id': 14331, 'relevance': 8, 'coherence': 6, 'fluency': 7}, {'id': 14347, 'relevance': 3, 'coherence': 9, 'fluency': 3}, {'id': 14348, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 14349, 'relevance': 3, 'coherence': 2, 'fluency': 3}, {'id': 14350, 'relevance': 3, 'coherence': 2, 'fluency': 3}, {'id': 14351, 'relevance': 3, 'coherence': 2, 'fluency': 2}, {'id': 16039, 'relevance': 5, 'coherence': 3, 'fluency': 3}, {'id': 14257, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 14258, 'relevance': 4, 'coherence': 3, 'fluency': 4}, {'id': 14259, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 14260, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 14261, 'relevance': 4, 'coherence': 3, 'fluency': 4}, {'id': 18668, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 15953, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 14527, 'relevance': 10, 'coherence': 8, 'fluency': 10}, {'id': 14528, 'relevance': 10, 'coherence': 8, 'fluency': 8}, {'id': 14529, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 14530, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 14531, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 16191, 'relevance': 8, 'coherence': 4, 'fluency': 4}, {'id': 14647, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 14648, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 14649, 'relevance': 8, 'coherence': 7, 'fluency': 6}, {'id': 14650, 'relevance': 8, 'coherence': 6, 'fluency': 7}, {'id': 14651, 'relevance': 8, 'coherence': 7, 'fluency': 8}, {'id': 14562, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 14563, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 14564, 'relevance': 5, 'coherence': 4, 'fluency': 4}, {'id': 14565, 'relevance': 5, 'coherence': 5, 'fluency': 5}, {'id': 14566, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 15673, 'relevance': 8, 'coherence': 6, 'fluency': 6}, {'id': 15640, 'relevance': 8, 'coherence': 5, 'fluency': 5}, {'id': 14522, 'relevance': 8, 'coherence': 7, 'fluency': 8}, {'id': 14523, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 14524, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 14525, 'relevance': 9, 'coherence': 8, 'fluency': 7}, {'id': 14526, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 15765, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 14609, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 14610, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 14611, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 14607, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 14608, 'relevance': 6, 'coherence': 3, 'fluency': 6}, {'id': 14612, 'relevance': 3, 'coherence': 6, 'fluency': 2}, {'id': 14613, 'relevance': 5, 'coherence': 10, 'fluency': 10}, {'id': 14614, 'relevance': 2, 'coherence': 10, 'fluency': 5}, {'id': 14615, 'relevance': 6, 'coherence': 7, 'fluency': 2}, {'id': 14616, 'relevance': 6, 'coherence': 2, 'fluency': 7}, {'id': 18566, 'relevance': 6, 'coherence': 6, 'fluency': 2}, {'id': 14807, 'relevance': 8, 'coherence': 8, 'fluency': 7}, {'id': 14808, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 14809, 'relevance': 6, 'coherence': 7, 'fluency': 8}, {'id': 14810, 'relevance': 6, 'coherence': 6, 'fluency': 7}, {'id': 14811, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 15882, 'relevance': 4, 'coherence': 5, 'fluency': 6}, {'id': 15781, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 14787, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 14788, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 14789, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 14790, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 14791, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 15952, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 14777, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 14778, 'relevance': 8, 'coherence': 6, 'fluency': 6}, {'id': 14779, 'relevance': 10, 'coherence': 9, 'fluency': 9}, {'id': 14780, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 14781, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 14747, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 14748, 'relevance': 6, 'coherence': 4, 'fluency': 4}, {'id': 14749, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 14750, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 16175, 'relevance': 10, 'coherence': 10, 'fluency': 10}, {'id': 14751, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 16185, 'relevance': 10, 'coherence': 8, 'fluency': 10}, {'id': 14752, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 14753, 'relevance': 6, 'coherence': 9, 'fluency': 6}, {'id': 14756, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 14754, 'relevance': 6, 'coherence': 3, 'fluency': 6}, {'id': 14755, 'relevance': 6, 'coherence': 3, 'fluency': 9}, {'id': 5191, 'relevance': 9, 'coherence': 8, 'fluency': 9}, {'id': 4296, 'relevance': 8, 'coherence': 6, 'fluency': 8}, {'id': 4297, 'relevance': 5, 'coherence': 6, 'fluency': 8}, {'id': 4298, 'relevance': 7, 'coherence': 7, 'fluency': 8}, {'id': 4299, 'relevance': 5, 'coherence': 7, 'fluency': 7}, {'id': 4300, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 14937, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 14938, 'relevance': 5, 'coherence': 4, 'fluency': 4}, {'id': 14939, 'relevance': 7, 'coherence': 6, 'fluency': 6}, {'id': 14940, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 14941, 'relevance': 8, 'coherence': 7, 'fluency': 7}, {'id': 16178, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 14866, 'relevance': 7, 'coherence': 7, 'fluency': 8}, {'id': 15795, 'relevance': 8, 'coherence': 9, 'fluency': 8}, {'id': 14864, 'relevance': 8, 'coherence': 7, 'fluency': 7}, {'id': 14865, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 14862, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 14863, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 16173, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 14907, 'relevance': 4, 'coherence': 6, 'fluency': 4}, {'id': 14908, 'relevance': 4, 'coherence': 6, 'fluency': 4}, {'id': 14909, 'relevance': 8, 'coherence': 6, 'fluency': 8}, {'id': 14910, 'relevance': 8, 'coherence': 8, 'fluency': 6}, {'id': 14911, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 14872, 'relevance': 6, 'coherence': 5, 'fluency': 6}, {'id': 14873, 'relevance': 8, 'coherence': 7, 'fluency': 7}, {'id': 14874, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 14875, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 14876, 'relevance': 6, 'coherence': 5, 'fluency': 5}, {'id': 16176, 'relevance': 6, 'coherence': 5, 'fluency': 5}, {'id': 5259, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 3976, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 3979, 'relevance': 7, 'coherence': 7, 'fluency': 9}, {'id': 3980, 'relevance': 9, 'coherence': 9, 'fluency': 10}, {'id': 3977, 'relevance': 9, 'coherence': 8, 'fluency': 9}, {'id': 3978, 'relevance': 9, 'coherence': 7, 'fluency': 10}, {'id': 15142, 'relevance': 3, 'coherence': 3, 'fluency': 2}, {'id': 15143, 'relevance': 3, 'coherence': 3, 'fluency': 2}, {'id': 15144, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 15145, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 15146, 'relevance': 1, 'coherence': 2, 'fluency': 2}, {'id': 18834, 'relevance': 3, 'coherence': 2, 'fluency': 2}, {'id': 15123, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 15124, 'relevance': 9, 'coherence': 8, 'fluency': 9}, {'id': 15125, 'relevance': 7, 'coherence': 7, 'fluency': 8}, {'id': 15126, 'relevance': 8, 'coherence': 6, 'fluency': 8}, {'id': 15792, 'relevance': 9, 'coherence': 8, 'fluency': 8}, {'id': 15122, 'relevance': 6, 'coherence': 6, 'fluency': 5}, {'id': 4278, 'relevance': 4, 'coherence': 3, 'fluency': 4}, {'id': 5185, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 4276, 'relevance': 6, 'coherence': 8, 'fluency': 8}, {'id': 4277, 'relevance': 8, 'coherence': 7, 'fluency': 8}, {'id': 4279, 'relevance': 6, 'coherence': 5, 'fluency': 6}, {'id': 4280, 'relevance': 7, 'coherence': 7, 'fluency': 6}, {'id': 15257, 'relevance': 4, 'coherence': 10, 'fluency': 3}, {'id': 15261, 'relevance': 3, 'coherence': 10, 'fluency': 10}, {'id': 18345, 'relevance': 6, 'coherence': 4, 'fluency': 4}, {'id': 15258, 'relevance': 4, 'coherence': 6, 'fluency': 4}, {'id': 15259, 'relevance': 5, 'coherence': 8, 'fluency': 8}, {'id': 15260, 'relevance': 10, 'coherence': 8, 'fluency': 6}, {'id': 16193, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 15497, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 15498, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 15499, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 15500, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 15501, 'relevance': 8, 'coherence': 7, 'fluency': 7}, {'id': 15379, 'relevance': 2, 'coherence': 9, 'fluency': 5}, {'id': 15380, 'relevance': 9, 'coherence': 7, 'fluency': 2}, {'id': 16245, 'relevance': 2, 'coherence': 2, 'fluency': 3}, {'id': 15378, 'relevance': 3, 'coherence': 3, 'fluency': 7}, {'id': 15381, 'relevance': 5, 'coherence': 7, 'fluency': 6}, {'id': 15377, 'relevance': 9, 'coherence': 7, 'fluency': 2}, {'id': 15517, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 15518, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 15519, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 15520, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 15521, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 18488, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 2366, 'relevance': 7, 'coherence': 6, 'fluency': 7}, {'id': 2367, 'relevance': 7, 'coherence': 8, 'fluency': 7}, {'id': 2370, 'relevance': 6, 'coherence': 6, 'fluency': 7}, {'id': 5165, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 2368, 'relevance': 5, 'coherence': 5, 'fluency': 5}, {'id': 2369, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 5189, 'relevance': 3, 'coherence': 4, 'fluency': 5}, {'id': 841, 'relevance': 3, 'coherence': 3, 'fluency': 4}, {'id': 842, 'relevance': 3, 'coherence': 4, 'fluency': 3}, {'id': 840, 'relevance': 4, 'coherence': 4, 'fluency': 6}, {'id': 843, 'relevance': 3, 'coherence': 3, 'fluency': 4}, {'id': 844, 'relevance': 3, 'coherence': 3, 'fluency': 4}, {'id': 3915, 'relevance': 5, 'coherence': 5, 'fluency': 6}, {'id': 3914, 'relevance': 2, 'coherence': 2, 'fluency': 3}, {'id': 3911, 'relevance': 8, 'coherence': 7, 'fluency': 8}, {'id': 3912, 'relevance': 4, 'coherence': 6, 'fluency': 6}, {'id': 3913, 'relevance': 5, 'coherence': 5, 'fluency': 7}, {'id': 5248, 'relevance': 7, 'coherence': 6, 'fluency': 9}, {'id': 7839, 'relevance': 6, 'coherence': 9, 'fluency': 9}, {'id': 7835, 'relevance': 3, 'coherence': 3, 'fluency': 6}, {'id': 7836, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 7837, 'relevance': 9, 'coherence': 6, 'fluency': 3}, {'id': 7838, 'relevance': 9, 'coherence': 3, 'fluency': 9}, {'id': 12317, 'relevance': 9, 'coherence': 3, 'fluency': 9}, {'id': 13677, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 13680, 'relevance': 9, 'coherence': 8, 'fluency': 8}, {'id': 13681, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 16005, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 13678, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 13679, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 12460, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 12457, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 12458, 'relevance': 6, 'coherence': 4, 'fluency': 6}, {'id': 15546, 'relevance': 8, 'coherence': 8, 'fluency': 10}, {'id': 12459, 'relevance': 8, 'coherence': 6, 'fluency': 8}, {'id': 12461, 'relevance': 8, 'coherence': 6, 'fluency': 6}, {'id': 15631, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 8070, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 8071, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 8072, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 8073, 'relevance': 4, 'coherence': 6, 'fluency': 6}, {'id': 8074, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 15577, 'relevance': 10, 'coherence': 10, 'fluency': 10}, {'id': 15578, 'relevance': 4, 'coherence': 6, 'fluency': 6}, {'id': 15579, 'relevance': 2, 'coherence': 2, 'fluency': 4}, {'id': 15580, 'relevance': 10, 'coherence': 8, 'fluency': 8}, {'id': 15581, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 16177, 'relevance': 10, 'coherence': 8, 'fluency': 8}, {'id': 14237, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 14238, 'relevance': 10, 'coherence': 10, 'fluency': 10}, {'id': 16088, 'relevance': 10, 'coherence': 9, 'fluency': 8}, {'id': 14239, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 14240, 'relevance': 10, 'coherence': 9, 'fluency': 9}, {'id': 14241, 'relevance': 9, 'coherence': 10, 'fluency': 10}, {'id': 15151, 'relevance': 8, 'coherence': 9, 'fluency': 8}, {'id': 15147, 'relevance': 8, 'coherence': 9, 'fluency': 9}, {'id': 15148, 'relevance': 9, 'coherence': 8, 'fluency': 5}, {'id': 15149, 'relevance': 7, 'coherence': 6, 'fluency': 8}, {'id': 15150, 'relevance': 6, 'coherence': 7, 'fluency': 8}, {'id': 15727, 'relevance': 8, 'coherence': 6, 'fluency': 7}, {'id': 15598, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 15597, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 15599, 'relevance': 3, 'coherence': 3, 'fluency': 9}, {'id': 15600, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 15601, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 15988, 'relevance': 3, 'coherence': 3, 'fluency': 9}, {'id': 14532, 'relevance': 8, 'coherence': 4, 'fluency': 5}, {'id': 14533, 'relevance': 9, 'coherence': 10, 'fluency': 3}, {'id': 14534, 'relevance': 2, 'coherence': 10, 'fluency': 2}, {'id': 14535, 'relevance': 6, 'coherence': 5, 'fluency': 4}, {'id': 14536, 'relevance': 2, 'coherence': 10, 'fluency': 10}, {'id': 15643, 'relevance': 4, 'coherence': 10, 'fluency': 10}, {'id': 11622, 'relevance': 3, 'coherence': 5, 'fluency': 8}, {'id': 11623, 'relevance': 5, 'coherence': 6, 'fluency': 7}, {'id': 11624, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 11625, 'relevance': 9, 'coherence': 8, 'fluency': 9}, {'id': 15623, 'relevance': 4, 'coherence': 5, 'fluency': 8}, {'id': 11621, 'relevance': 5, 'coherence': 7, 'fluency': 8}, {'id': 15610, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 12281, 'relevance': 10, 'coherence': 10, 'fluency': 10}, {'id': 12282, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 12283, 'relevance': 8, 'coherence': 10, 'fluency': 8}, {'id': 12284, 'relevance': 10, 'coherence': 10, 'fluency': 8}, {'id': 12285, 'relevance': 8, 'coherence': 10, 'fluency': 10}, {'id': 12542, 'relevance': 10, 'coherence': 8, 'fluency': 8}, {'id': 12543, 'relevance': 8, 'coherence': 10, 'fluency': 8}, {'id': 12544, 'relevance': 6, 'coherence': 8, 'fluency': 6}, {'id': 12545, 'relevance': 6, 'coherence': 6, 'fluency': 8}, {'id': 12546, 'relevance': 6, 'coherence': 6, 'fluency': 8}, {'id': 15633, 'relevance': 10, 'coherence': 10, 'fluency': 10}, {'id': 9285, 'relevance': 9, 'coherence': 8, 'fluency': 9}, {'id': 9286, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 9287, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 9289, 'relevance': 3, 'coherence': 4, 'fluency': 4}, {'id': 9288, 'relevance': 8, 'coherence': 8, 'fluency': 7}, {'id': 15613, 'relevance': 7, 'coherence': 8, 'fluency': 7}, {'id': 15660, 'relevance': 7, 'coherence': 6, 'fluency': 6}, {'id': 14942, 'relevance': 6, 'coherence': 5, 'fluency': 6}, {'id': 14943, 'relevance': 6, 'coherence': 5, 'fluency': 6}, {'id': 14944, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 14945, 'relevance': 8, 'coherence': 8, 'fluency': 7}, {'id': 14946, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 15535, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 14997, 'relevance': 3, 'coherence': 4, 'fluency': 4}, {'id': 14998, 'relevance': 4, 'coherence': 3, 'fluency': 4}, {'id': 14999, 'relevance': 3, 'coherence': 3, 'fluency': 4}, {'id': 15000, 'relevance': 4, 'coherence': 3, 'fluency': 5}, {'id': 15001, 'relevance': 4, 'coherence': 4, 'fluency': 5}, {'id': 15647, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 14672, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 14673, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 14674, 'relevance': 6, 'coherence': 6, 'fluency': 7}, {'id': 14675, 'relevance': 8, 'coherence': 8, 'fluency': 7}, {'id': 14676, 'relevance': 5, 'coherence': 5, 'fluency': 5}, {'id': 8265, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 8266, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 8267, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 15672, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 8268, 'relevance': 5, 'coherence': 5, 'fluency': 5}, {'id': 8269, 'relevance': 5, 'coherence': 5, 'fluency': 4}, {'id': 5960, 'relevance': 7, 'coherence': 7, 'fluency': 2}, {'id': 5961, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 5962, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 5963, 'relevance': 7, 'coherence': 7, 'fluency': 3}, {'id': 5964, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 15662, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 12206, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 12207, 'relevance': 5, 'coherence': 4, 'fluency': 3}, {'id': 12208, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 12209, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 12210, 'relevance': 8, 'coherence': 7, 'fluency': 8}, {'id': 15668, 'relevance': 7, 'coherence': 8, 'fluency': 8}, {'id': 15676, 'relevance': 8, 'coherence': 6, 'fluency': 6}, {'id': 15474, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 15475, 'relevance': 8, 'coherence': 6, 'fluency': 7}, {'id': 15476, 'relevance': 8, 'coherence': 7, 'fluency': 8}, {'id': 15472, 'relevance': 8, 'coherence': 8, 'fluency': 7}, {'id': 15473, 'relevance': 8, 'coherence': 9, 'fluency': 8}, {'id': 12807, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 12808, 'relevance': 8, 'coherence': 8, 'fluency': 7}, {'id': 12809, 'relevance': 8, 'coherence': 6, 'fluency': 8}, {'id': 12810, 'relevance': 9, 'coherence': 7, 'fluency': 8}, {'id': 15658, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 12811, 'relevance': 8, 'coherence': 5, 'fluency': 5}, {'id': 10149, 'relevance': 8, 'coherence': 6, 'fluency': 6}, {'id': 10150, 'relevance': 4, 'coherence': 3, 'fluency': 3}, {'id': 15698, 'relevance': 6, 'coherence': 6, 'fluency': 4}, {'id': 10146, 'relevance': 8, 'coherence': 10, 'fluency': 10}, {'id': 10147, 'relevance': 10, 'coherence': 10, 'fluency': 8}, {'id': 10148, 'relevance': 8, 'coherence': 6, 'fluency': 8}, {'id': 15747, 'relevance': 5, 'coherence': 5, 'fluency': 5}, {'id': 10035, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 10036, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 10037, 'relevance': 7, 'coherence': 6, 'fluency': 6}, {'id': 10038, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 10039, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 7315, 'relevance': 3, 'coherence': 3, 'fluency': 8}, {'id': 7316, 'relevance': 3, 'coherence': 3, 'fluency': 7}, {'id': 7317, 'relevance': 8, 'coherence': 8, 'fluency': 3}, {'id': 7318, 'relevance': 3, 'coherence': 7, 'fluency': 3}, {'id': 7319, 'relevance': 3, 'coherence': 3, 'fluency': 7}, {'id': 15763, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 8340, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 8341, 'relevance': 5, 'coherence': 3, 'fluency': 3}, {'id': 8342, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 8343, 'relevance': 3, 'coherence': 3, 'fluency': 10}, {'id': 8344, 'relevance': 5, 'coherence': 3, 'fluency': 3}, {'id': 15759, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 5764, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 5760, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 5761, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 5762, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 5763, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 15776, 'relevance': 8, 'coherence': 7, 'fluency': 7}, {'id': 12384, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 12386, 'relevance': 8, 'coherence': 7, 'fluency': 7}, {'id': 12382, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 12383, 'relevance': 5, 'coherence': 6, 'fluency': 5}, {'id': 12385, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 15796, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 11441, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 11442, 'relevance': 10, 'coherence': 10, 'fluency': 10}, {'id': 11443, 'relevance': 10, 'coherence': 10, 'fluency': 10}, {'id': 11444, 'relevance': 10, 'coherence': 10, 'fluency': 10}, {'id': 11445, 'relevance': 10, 'coherence': 10, 'fluency': 10}, {'id': 15783, 'relevance': 3, 'coherence': 10, 'fluency': 10}, {'id': 15784, 'relevance': 9, 'coherence': 8, 'fluency': 8}, {'id': 14847, 'relevance': 10, 'coherence': 10, 'fluency': 8}, {'id': 14848, 'relevance': 10, 'coherence': 10, 'fluency': 10}, {'id': 14849, 'relevance': 10, 'coherence': 9, 'fluency': 9}, {'id': 14850, 'relevance': 4, 'coherence': 3, 'fluency': 4}, {'id': 14851, 'relevance': 6, 'coherence': 7, 'fluency': 6}, {'id': 15537, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 11261, 'relevance': 4, 'coherence': 5, 'fluency': 4}, {'id': 11262, 'relevance': 4, 'coherence': 5, 'fluency': 5}, {'id': 11263, 'relevance': 5, 'coherence': 5, 'fluency': 5}, {'id': 11264, 'relevance': 5, 'coherence': 5, 'fluency': 5}, {'id': 11265, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 6760, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 6761, 'relevance': 9, 'coherence': 8, 'fluency': 7}, {'id': 6762, 'relevance': 7, 'coherence': 8, 'fluency': 8}, {'id': 6763, 'relevance': 10, 'coherence': 9, 'fluency': 10}, {'id': 6764, 'relevance': 10, 'coherence': 9, 'fluency': 10}, {'id': 15773, 'relevance': 7, 'coherence': 6, 'fluency': 8}, {'id': 6620, 'relevance': 2, 'coherence': 2, 'fluency': 4}, {'id': 6621, 'relevance': 4, 'coherence': 6, 'fluency': 6}, {'id': 6622, 'relevance': 4, 'coherence': 6, 'fluency': 6}, {'id': 6623, 'relevance': 10, 'coherence': 8, 'fluency': 8}, {'id': 6624, 'relevance': 10, 'coherence': 8, 'fluency': 10}, {'id': 15724, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 10641, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 10642, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 10643, 'relevance': 7, 'coherence': 7, 'fluency': 2}, {'id': 10644, 'relevance': 6, 'coherence': 6, 'fluency': 2}, {'id': 10645, 'relevance': 2, 'coherence': 6, 'fluency': 2}, {'id': 15770, 'relevance': 10, 'coherence': 6, 'fluency': 6}, {'id': 12325, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 6190, 'relevance': 7, 'coherence': 6, 'fluency': 6}, {'id': 6192, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 6193, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 6191, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 6194, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 15901, 'relevance': 10, 'coherence': 10, 'fluency': 10}, {'id': 14732, 'relevance': 8, 'coherence': 10, 'fluency': 8}, {'id': 14733, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 14734, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 14735, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 14736, 'relevance': 10, 'coherence': 8, 'fluency': 8}, {'id': 9260, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 9261, 'relevance': 2, 'coherence': 2, 'fluency': 1}, {'id': 9264, 'relevance': 1, 'coherence': 2, 'fluency': 2}, {'id': 15852, 'relevance': 1, 'coherence': 1, 'fluency': 2}, {'id': 9262, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 9263, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 9866, 'relevance': 1, 'coherence': 2, 'fluency': 2}, {'id': 9867, 'relevance': 1, 'coherence': 3, 'fluency': 2}, {'id': 9865, 'relevance': 2, 'coherence': 3, 'fluency': 1}, {'id': 9868, 'relevance': 1, 'coherence': 2, 'fluency': 2}, {'id': 9869, 'relevance': 2, 'coherence': 1, 'fluency': 2}, {'id': 15910, 'relevance': 1, 'coherence': 1, 'fluency': 2}, {'id': 15903, 'relevance': 4, 'coherence': 3, 'fluency': 4}, {'id': 8120, 'relevance': 4, 'coherence': 5, 'fluency': 4}, {'id': 8121, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 8122, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 8123, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 8124, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 12692, 'relevance': 8, 'coherence': 2, 'fluency': 10}, {'id': 12696, 'relevance': 2, 'coherence': 10, 'fluency': 7}, {'id': 12693, 'relevance': 4, 'coherence': 6, 'fluency': 4}, {'id': 12694, 'relevance': 3, 'coherence': 3, 'fluency': 10}, {'id': 15847, 'relevance': 9, 'coherence': 3, 'fluency': 4}, {'id': 12695, 'relevance': 2, 'coherence': 8, 'fluency': 10}, {'id': 6550, 'relevance': 8, 'coherence': 8, 'fluency': 6}, {'id': 6551, 'relevance': 8, 'coherence': 10, 'fluency': 8}, {'id': 6552, 'relevance': 8, 'coherence': 6, 'fluency': 10}, {'id': 6553, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 6554, 'relevance': 8, 'coherence': 8, 'fluency': 6}, {'id': 15971, 'relevance': 4, 'coherence': 4, 'fluency': 3}, {'id': 16041, 'relevance': 4, 'coherence': 6, 'fluency': 4}, {'id': 6230, 'relevance': 4, 'coherence': 4, 'fluency': 2}, {'id': 6231, 'relevance': 6, 'coherence': 4, 'fluency': 2}, {'id': 6232, 'relevance': 6, 'coherence': 2, 'fluency': 6}, {'id': 6233, 'relevance': 4, 'coherence': 6, 'fluency': 2}, {'id': 6234, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 9840, 'relevance': 7, 'coherence': 7, 'fluency': 8}, {'id': 15635, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 9841, 'relevance': 8, 'coherence': 7, 'fluency': 8}, {'id': 9842, 'relevance': 9, 'coherence': 8, 'fluency': 8}, {'id': 9843, 'relevance': 10, 'coherence': 10, 'fluency': 8}, {'id': 9844, 'relevance': 8, 'coherence': 7, 'fluency': 7}, {'id': 5176, 'relevance': 5, 'coherence': 4, 'fluency': 5}, {'id': 750, 'relevance': 8, 'coherence': 8, 'fluency': 7}, {'id': 751, 'relevance': 6, 'coherence': 7, 'fluency': 8}, {'id': 752, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 753, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 754, 'relevance': 8, 'coherence': 7, 'fluency': 8}, {'id': 8467, 'relevance': 8, 'coherence': 6, 'fluency': 4}, {'id': 16046, 'relevance': 6, 'coherence': 9, 'fluency': 6}, {'id': 8465, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 8466, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 8468, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 8469, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 5179, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 360, 'relevance': 4, 'coherence': 6, 'fluency': 8}, {'id': 361, 'relevance': 8, 'coherence': 7, 'fluency': 8}, {'id': 362, 'relevance': 8, 'coherence': 7, 'fluency': 7}, {'id': 363, 'relevance': 7, 'coherence': 7, 'fluency': 8}, {'id': 364, 'relevance': 9, 'coherence': 8, 'fluency': 9}, {'id': 355, 'relevance': 5, 'coherence': 5, 'fluency': 6}, {'id': 5180, 'relevance': 7, 'coherence': 5, 'fluency': 5}, {'id': 359, 'relevance': 9, 'coherence': 8, 'fluency': 8}, {'id': 356, 'relevance': 9, 'coherence': 8, 'fluency': 8}, {'id': 357, 'relevance': 7, 'coherence': 6, 'fluency': 8}, {'id': 358, 'relevance': 8, 'coherence': 7, 'fluency': 8}, {'id': 550, 'relevance': 8, 'coherence': 9, 'fluency': 8}, {'id': 551, 'relevance': 9, 'coherence': 8, 'fluency': 8}, {'id': 552, 'relevance': 9, 'coherence': 8, 'fluency': 8}, {'id': 553, 'relevance': 7, 'coherence': 7, 'fluency': 8}, {'id': 554, 'relevance': 9, 'coherence': 8, 'fluency': 8}, {'id': 5172, 'relevance': 9, 'coherence': 8, 'fluency': 8}, {'id': 16295, 'relevance': 8, 'coherence': 8, 'fluency': 7}, {'id': 16296, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 16297, 'relevance': 9, 'coherence': 8, 'fluency': 8}, {'id': 16298, 'relevance': 9, 'coherence': 8, 'fluency': 10}, {'id': 16299, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 18397, 'relevance': 8, 'coherence': 7, 'fluency': 8}, {'id': 18445, 'relevance': 8, 'coherence': 7, 'fluency': 8}, {'id': 16301, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 16302, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 16300, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 16303, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 16304, 'relevance': 8, 'coherence': 7, 'fluency': 8}, {'id': 11591, 'relevance': 8, 'coherence': 7, 'fluency': 7}, {'id': 11593, 'relevance': 7, 'coherence': 6, 'fluency': 7}, {'id': 11594, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 11595, 'relevance': 7, 'coherence': 6, 'fluency': 6}, {'id': 15839, 'relevance': 4, 'coherence': 3, 'fluency': 3}, {'id': 11592, 'relevance': 6, 'coherence': 3, 'fluency': 4}, {'id': 16213, 'relevance': 6, 'coherence': 4, 'fluency': 10}, {'id': 8500, 'relevance': 4, 'coherence': 6, 'fluency': 6}, {'id': 8501, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 8502, 'relevance': 4, 'coherence': 8, 'fluency': 8}, {'id': 8503, 'relevance': 4, 'coherence': 6, 'fluency': 8}, {'id': 8504, 'relevance': 10, 'coherence': 10, 'fluency': 10}, {'id': 16275, 'relevance': 8, 'coherence': 9, 'fluency': 8}, {'id': 16276, 'relevance': 9, 'coherence': 8, 'fluency': 8}, {'id': 16277, 'relevance': 9, 'coherence': 8, 'fluency': 9}, {'id': 16278, 'relevance': 9, 'coherence': 8, 'fluency': 8}, {'id': 16279, 'relevance': 9, 'coherence': 8, 'fluency': 8}, {'id': 18667, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 6512, 'relevance': 0, 'coherence': 0, 'fluency': 0}, {'id': 16234, 'relevance': 3, 'coherence': 2, 'fluency': 2}, {'id': 6511, 'relevance': 4, 'coherence': 3, 'fluency': 1}, {'id': 6513, 'relevance': 3, 'coherence': 3, 'fluency': 1}, {'id': 6510, 'relevance': 1, 'coherence': 1, 'fluency': 1}, {'id': 6514, 'relevance': 1, 'coherence': 2, 'fluency': 2}, {'id': 15355, 'relevance': 4, 'coherence': 4, 'fluency': 2}, {'id': 15356, 'relevance': 4, 'coherence': 4, 'fluency': 2}, {'id': 16242, 'relevance': 2, 'coherence': 2, 'fluency': 1}, {'id': 15353, 'relevance': 2, 'coherence': 4, 'fluency': 4}, {'id': 15354, 'relevance': 2, 'coherence': 4, 'fluency': 4}, {'id': 15352, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 7710, 'relevance': 2, 'coherence': 2, 'fluency': 1}, {'id': 7712, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 7713, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 7714, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 16223, 'relevance': 3, 'coherence': 1, 'fluency': 3}, {'id': 7711, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 18459, 'relevance': 8, 'coherence': 7, 'fluency': 8}, {'id': 16570, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 16571, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 16572, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 16573, 'relevance': 8, 'coherence': 7, 'fluency': 7}, {'id': 16574, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 18464, 'relevance': 8, 'coherence': 6, 'fluency': 6}, {'id': 16675, 'relevance': 8, 'coherence': 6, 'fluency': 7}, {'id': 16676, 'relevance': 9, 'coherence': 9, 'fluency': 8}, {'id': 16677, 'relevance': 8, 'coherence': 7, 'fluency': 6}, {'id': 16678, 'relevance': 8, 'coherence': 7, 'fluency': 7}, {'id': 16679, 'relevance': 8, 'coherence': 7, 'fluency': 7}, {'id': 18497, 'relevance': 6, 'coherence': 5, 'fluency': 7}, {'id': 16535, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 16536, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 16537, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 16538, 'relevance': 6, 'coherence': 5, 'fluency': 6}, {'id': 16539, 'relevance': 8, 'coherence': 9, 'fluency': 7}, {'id': 16765, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 16766, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 16767, 'relevance': 5, 'coherence': 5, 'fluency': 6}, {'id': 16768, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 16769, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 18766, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 18299, 'relevance': 8, 'coherence': 7, 'fluency': 7}, {'id': 16790, 'relevance': 8, 'coherence': 7, 'fluency': 8}, {'id': 16791, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 16792, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 16793, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 16794, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 16824, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 16820, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 16821, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 16822, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 16823, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 18400, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 16900, 'relevance': 2, 'coherence': 1, 'fluency': 1}, {'id': 16901, 'relevance': 1, 'coherence': 3, 'fluency': 1}, {'id': 16902, 'relevance': 1, 'coherence': 1, 'fluency': 1}, {'id': 16904, 'relevance': 1, 'coherence': 1, 'fluency': 1}, {'id': 18327, 'relevance': 2, 'coherence': 3, 'fluency': 3}, {'id': 16903, 'relevance': 1, 'coherence': 1, 'fluency': 1}, {'id': 18457, 'relevance': 6, 'coherence': 6, 'fluency': 7}, {'id': 16890, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 16891, 'relevance': 7, 'coherence': 6, 'fluency': 6}, {'id': 16892, 'relevance': 6, 'coherence': 8, 'fluency': 7}, {'id': 16893, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 16894, 'relevance': 8, 'coherence': 6, 'fluency': 7}, {'id': 17155, 'relevance': 9, 'coherence': 9, 'fluency': 8}, {'id': 17156, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 17157, 'relevance': 9, 'coherence': 8, 'fluency': 8}, {'id': 17158, 'relevance': 9, 'coherence': 8, 'fluency': 8}, {'id': 18390, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 17159, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 18378, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 17115, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 17116, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 17117, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 17118, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 17119, 'relevance': 2, 'coherence': 3, 'fluency': 3}, {'id': 17144, 'relevance': 8, 'coherence': 5, 'fluency': 7}, {'id': 17140, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 17141, 'relevance': 8, 'coherence': 7, 'fluency': 7}, {'id': 17142, 'relevance': 8, 'coherence': 6, 'fluency': 7}, {'id': 17143, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 18394, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 17154, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 17152, 'relevance': 10, 'coherence': 10, 'fluency': 10}, {'id': 17150, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 17151, 'relevance': 7, 'coherence': 3, 'fluency': 3}, {'id': 17153, 'relevance': 2, 'coherence': 10, 'fluency': 10}, {'id': 18428, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 17174, 'relevance': 8, 'coherence': 6, 'fluency': 6}, {'id': 17170, 'relevance': 6, 'coherence': 5, 'fluency': 4}, {'id': 17171, 'relevance': 10, 'coherence': 10, 'fluency': 10}, {'id': 17172, 'relevance': 9, 'coherence': 7, 'fluency': 8}, {'id': 17173, 'relevance': 10, 'coherence': 8, 'fluency': 8}, {'id': 18434, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 17149, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 17145, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 17146, 'relevance': 8, 'coherence': 7, 'fluency': 6}, {'id': 17147, 'relevance': 6, 'coherence': 5, 'fluency': 5}, {'id': 17148, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 18441, 'relevance': 6, 'coherence': 5, 'fluency': 6}, {'id': 17367, 'relevance': 5, 'coherence': 5, 'fluency': 3}, {'id': 17368, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 17369, 'relevance': 2, 'coherence': 4, 'fluency': 3}, {'id': 17365, 'relevance': 5, 'coherence': 5, 'fluency': 5}, {'id': 17366, 'relevance': 5, 'coherence': 5, 'fluency': 5}, {'id': 18824, 'relevance': 3, 'coherence': 4, 'fluency': 4}, {'id': 17330, 'relevance': 9, 'coherence': 5, 'fluency': 5}, {'id': 17331, 'relevance': 4, 'coherence': 4, 'fluency': 5}, {'id': 17332, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 17333, 'relevance': 8, 'coherence': 6, 'fluency': 6}, {'id': 18556, 'relevance': 8, 'coherence': 5, 'fluency': 6}, {'id': 17334, 'relevance': 10, 'coherence': 10, 'fluency': 10}, {'id': 17295, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 17296, 'relevance': 8, 'coherence': 8, 'fluency': 7}, {'id': 17297, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 17298, 'relevance': 8, 'coherence': 8, 'fluency': 7}, {'id': 17299, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 18356, 'relevance': 8, 'coherence': 9, 'fluency': 8}, {'id': 17275, 'relevance': 8, 'coherence': 8, 'fluency': 7}, {'id': 17276, 'relevance': 10, 'coherence': 10, 'fluency': 10}, {'id': 17277, 'relevance': 7, 'coherence': 7, 'fluency': 6}, {'id': 18463, 'relevance': 8, 'coherence': 7, 'fluency': 7}, {'id': 17278, 'relevance': 9, 'coherence': 8, 'fluency': 8}, {'id': 17279, 'relevance': 8, 'coherence': 8, 'fluency': 7}, {'id': 18294, 'relevance': 7, 'coherence': 6, 'fluency': 6}, {'id': 17305, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 17306, 'relevance': 4, 'coherence': 3, 'fluency': 3}, {'id': 17307, 'relevance': 2, 'coherence': 2, 'fluency': 4}, {'id': 17308, 'relevance': 3, 'coherence': 3, 'fluency': 2}, {'id': 17309, 'relevance': 9, 'coherence': 8, 'fluency': 8}, {'id': 17350, 'relevance': 6, 'coherence': 5, 'fluency': 6}, {'id': 17351, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 17352, 'relevance': 9, 'coherence': 9, 'fluency': 8}, {'id': 17353, 'relevance': 4, 'coherence': 4, 'fluency': 5}, {'id': 17354, 'relevance': 5, 'coherence': 5, 'fluency': 4}, {'id': 18546, 'relevance': 10, 'coherence': 10, 'fluency': 10}, {'id': 17272, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 17273, 'relevance': 9, 'coherence': 8, 'fluency': 8}, {'id': 17274, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 17270, 'relevance': 10, 'coherence': 10, 'fluency': 10}, {'id': 17271, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 18547, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 17300, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 17301, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 17302, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 17303, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 17304, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 18586, 'relevance': 8, 'coherence': 4, 'fluency': 4}, {'id': 17356, 'relevance': 3, 'coherence': 9, 'fluency': 3}, {'id': 17357, 'relevance': 9, 'coherence': 3, 'fluency': 3}, {'id': 17355, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 17358, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 17359, 'relevance': 3, 'coherence': 6, 'fluency': 6}, {'id': 18768, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 17545, 'relevance': 8, 'coherence': 7, 'fluency': 5}, {'id': 17546, 'relevance': 7, 'coherence': 8, 'fluency': 8}, {'id': 17547, 'relevance': 2, 'coherence': 2, 'fluency': 7}, {'id': 17548, 'relevance': 10, 'coherence': 10, 'fluency': 10}, {'id': 18456, 'relevance': 6, 'coherence': 7, 'fluency': 7}, {'id': 17549, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 17530, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 17531, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 17532, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 17533, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 17534, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 18338, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 17515, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 17516, 'relevance': 7, 'coherence': 8, 'fluency': 7}, {'id': 17517, 'relevance': 7, 'coherence': 6, 'fluency': 8}, {'id': 17518, 'relevance': 8, 'coherence': 7, 'fluency': 8}, {'id': 17519, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 18560, 'relevance': 6, 'coherence': 8, 'fluency': 8}, {'id': 17445, 'relevance': 0, 'coherence': 0, 'fluency': 0}, {'id': 17446, 'relevance': 0, 'coherence': 0, 'fluency': 0}, {'id': 17447, 'relevance': 0, 'coherence': 0, 'fluency': 0}, {'id': 17448, 'relevance': 0, 'coherence': 0, 'fluency': 0}, {'id': 17449, 'relevance': 0, 'coherence': 0, 'fluency': 0}, {'id': 18439, 'relevance': 0, 'coherence': 0, 'fluency': 0}, {'id': 17509, 'relevance': 4, 'coherence': 3, 'fluency': 4}, {'id': 18429, 'relevance': 6, 'coherence': 5, 'fluency': 6}, {'id': 17505, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 17506, 'relevance': 8, 'coherence': 7, 'fluency': 8}, {'id': 17507, 'relevance': 7, 'coherence': 7, 'fluency': 8}, {'id': 17508, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 17580, 'relevance': 7, 'coherence': 6, 'fluency': 7}, {'id': 17581, 'relevance': 8, 'coherence': 6, 'fluency': 7}, {'id': 17582, 'relevance': 8, 'coherence': 8, 'fluency': 6}, {'id': 18585, 'relevance': 6, 'coherence': 5, 'fluency': 6}, {'id': 17583, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 17584, 'relevance': 7, 'coherence': 6, 'fluency': 7}, {'id': 18348, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 17889, 'relevance': 8, 'coherence': 8, 'fluency': 6}, {'id': 17885, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 17886, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 17887, 'relevance': 10, 'coherence': 10, 'fluency': 10}, {'id': 17888, 'relevance': 6, 'coherence': 5, 'fluency': 5}, {'id': 17845, 'relevance': 8, 'coherence': 6, 'fluency': 7}, {'id': 17846, 'relevance': 8, 'coherence': 6, 'fluency': 8}, {'id': 17847, 'relevance': 8, 'coherence': 7, 'fluency': 6}, {'id': 17848, 'relevance': 8, 'coherence': 5, 'fluency': 6}, {'id': 17849, 'relevance': 9, 'coherence': 8, 'fluency': 7}, {'id': 18838, 'relevance': 6, 'coherence': 7, 'fluency': 5}, {'id': 17860, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 17861, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 17862, 'relevance': 8, 'coherence': 6, 'fluency': 6}, {'id': 17863, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 18384, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 17864, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 18385, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 17840, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 17841, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 17842, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 17843, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 17844, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 17754, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 17750, 'relevance': 8, 'coherence': 9, 'fluency': 8}, {'id': 17751, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 17752, 'relevance': 8, 'coherence': 8, 'fluency': 7}, {'id': 17753, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 18406, 'relevance': 8, 'coherence': 9, 'fluency': 8}, {'id': 18455, 'relevance': 4, 'coherence': 4, 'fluency': 5}, {'id': 17765, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 17766, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 17767, 'relevance': 4, 'coherence': 4, 'fluency': 5}, {'id': 17768, 'relevance': 3, 'coherence': 3, 'fluency': 4}, {'id': 17769, 'relevance': 3, 'coherence': 4, 'fluency': 4}, {'id': 18055, 'relevance': 3, 'coherence': 7, 'fluency': 8}, {'id': 18056, 'relevance': 3, 'coherence': 10, 'fluency': 3}, {'id': 18057, 'relevance': 3, 'coherence': 2, 'fluency': 2}, {'id': 18058, 'relevance': 3, 'coherence': 2, 'fluency': 3}, {'id': 18059, 'relevance': 3, 'coherence': 2, 'fluency': 3}, {'id': 18446, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 18000, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 18001, 'relevance': 10, 'coherence': 8, 'fluency': 8}, {'id': 18002, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 18003, 'relevance': 8, 'coherence': 6, 'fluency': 8}, {'id': 18461, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 18004, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 17895, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 17896, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 17897, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 17898, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 17899, 'relevance': 5, 'coherence': 5, 'fluency': 5}, {'id': 18494, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 17910, 'relevance': 8, 'coherence': 8, 'fluency': 7}, {'id': 17911, 'relevance': 9, 'coherence': 8, 'fluency': 9}, {'id': 17912, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 17913, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 18496, 'relevance': 8, 'coherence': 7, 'fluency': 7}, {'id': 17914, 'relevance': 8, 'coherence': 8, 'fluency': 7}, {'id': 18503, 'relevance': 8, 'coherence': 7, 'fluency': 7}, {'id': 17985, 'relevance': 9, 'coherence': 8, 'fluency': 9}, {'id': 17986, 'relevance': 7, 'coherence': 5, 'fluency': 5}, {'id': 17987, 'relevance': 8, 'coherence': 7, 'fluency': 7}, {'id': 17988, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 17989, 'relevance': 10, 'coherence': 10, 'fluency': 10}, {'id': 17930, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 17931, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 17932, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 17933, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 17934, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 18543, 'relevance': 5, 'coherence': 5, 'fluency': 5}, {'id': 17935, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 17936, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 17937, 'relevance': 8, 'coherence': 7, 'fluency': 7}, {'id': 17938, 'relevance': 8, 'coherence': 7, 'fluency': 7}, {'id': 17939, 'relevance': 8, 'coherence': 8, 'fluency': 6}, {'id': 18553, 'relevance': 8, 'coherence': 9, 'fluency': 8}, {'id': 18020, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 18021, 'relevance': 9, 'coherence': 8, 'fluency': 10}, {'id': 18022, 'relevance': 8, 'coherence': 7, 'fluency': 8}, {'id': 18023, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 18729, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 18024, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 18401, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 18210, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 18211, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 18212, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 18213, 'relevance': 5, 'coherence': 6, 'fluency': 6}, {'id': 18214, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 18105, 'relevance': 9, 'coherence': 9, 'fluency': 8}, {'id': 18106, 'relevance': 5, 'coherence': 6, 'fluency': 5}, {'id': 18107, 'relevance': 10, 'coherence': 9, 'fluency': 10}, {'id': 18108, 'relevance': 8, 'coherence': 7, 'fluency': 7}, {'id': 18492, 'relevance': 7, 'coherence': 6, 'fluency': 6}, {'id': 18109, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 18120, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 18638, 'relevance': 4, 'coherence': 5, 'fluency': 5}, {'id': 18124, 'relevance': 7, 'coherence': 5, 'fluency': 6}, {'id': 18121, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 18122, 'relevance': 5, 'coherence': 5, 'fluency': 5}, {'id': 18123, 'relevance': 8, 'coherence': 6, 'fluency': 7}, {'id': 18748, 'relevance': 3, 'coherence': 4, 'fluency': 4}, {'id': 18175, 'relevance': 4, 'coherence': 5, 'fluency': 5}, {'id': 18176, 'relevance': 3, 'coherence': 3, 'fluency': 4}, {'id': 18177, 'relevance': 2, 'coherence': 2, 'fluency': 3}, {'id': 18178, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 18179, 'relevance': 3, 'coherence': 4, 'fluency': 4}, {'id': 7731, 'relevance': 6, 'coherence': 4, 'fluency': 6}, {'id': 7732, 'relevance': 4, 'coherence': 2, 'fluency': 4}, {'id': 7733, 'relevance': 4, 'coherence': 2, 'fluency': 2}, {'id': 7734, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 16224, 'relevance': 4, 'coherence': 4, 'fluency': 8}, {'id': 7730, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 18291, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 18240, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 18241, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 18242, 'relevance': 8, 'coherence': 7, 'fluency': 8}, {'id': 18243, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 18244, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 18245, 'relevance': 6, 'coherence': 8, 'fluency': 6}, {'id': 18246, 'relevance': 9, 'coherence': 10, 'fluency': 9}, {'id': 18247, 'relevance': 6, 'coherence': 5, 'fluency': 5}, {'id': 18248, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 18249, 'relevance': 8, 'coherence': 5, 'fluency': 6}, {'id': 18371, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 18290, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 17165, 'relevance': 8, 'coherence': 7, 'fluency': 7}, {'id': 17166, 'relevance': 4, 'coherence': 4, 'fluency': 5}, {'id': 17167, 'relevance': 5, 'coherence': 6, 'fluency': 6}, {'id': 17168, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 17169, 'relevance': 6, 'coherence': 5, 'fluency': 6}, {'id': 16715, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 16716, 'relevance': 2, 'coherence': 2, 'fluency': 6}, {'id': 16717, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 16719, 'relevance': 2, 'coherence': 2, 'fluency': 7}, {'id': 16718, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 18285, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 18298, 'relevance': 7, 'coherence': 8, 'fluency': 8}, {'id': 17865, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 17866, 'relevance': 8, 'coherence': 7, 'fluency': 8}, {'id': 17867, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 17868, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 17869, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 15877, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 13392, 'relevance': 3, 'coherence': 9, 'fluency': 3}, {'id': 13393, 'relevance': 3, 'coherence': 3, 'fluency': 6}, {'id': 13394, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 13395, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 13396, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 18308, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 17520, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 17521, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 17522, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 17523, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 17524, 'relevance': 8, 'coherence': 7, 'fluency': 8}, {'id': 9470, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 9471, 'relevance': 8, 'coherence': 7, 'fluency': 8}, {'id': 9472, 'relevance': 8, 'coherence': 7, 'fluency': 7}, {'id': 9473, 'relevance': 6, 'coherence': 8, 'fluency': 8}, {'id': 18305, 'relevance': 7, 'coherence': 6, 'fluency': 8}, {'id': 9474, 'relevance': 8, 'coherence': 7, 'fluency': 7}, {'id': 9762, 'relevance': 8, 'coherence': 6, 'fluency': 6}, {'id': 9760, 'relevance': 8, 'coherence': 6, 'fluency': 8}, {'id': 9761, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 9763, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 9764, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 18312, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 6682, 'relevance': 0, 'coherence': 0, 'fluency': 0}, {'id': 6680, 'relevance': 1, 'coherence': 2, 'fluency': 1}, {'id': 6681, 'relevance': 2, 'coherence': 2, 'fluency': 1}, {'id': 6683, 'relevance': 2, 'coherence': 2, 'fluency': 1}, {'id': 6684, 'relevance': 1, 'coherence': 1, 'fluency': 1}, {'id': 18336, 'relevance': 1, 'coherence': 1, 'fluency': 2}, {'id': 18389, 'relevance': 8, 'coherence': 7, 'fluency': 7}, {'id': 18119, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 18115, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 18116, 'relevance': 6, 'coherence': 5, 'fluency': 5}, {'id': 18117, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 18118, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 16850, 'relevance': 5, 'coherence': 5, 'fluency': 5}, {'id': 16851, 'relevance': 10, 'coherence': 10, 'fluency': 10}, {'id': 16852, 'relevance': 5, 'coherence': 5, 'fluency': 5}, {'id': 16853, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 16854, 'relevance': 8, 'coherence': 7, 'fluency': 7}, {'id': 18398, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 17579, 'relevance': 8, 'coherence': 7, 'fluency': 8}, {'id': 18347, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 17575, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 17576, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 17577, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 17578, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 6375, 'relevance': 8, 'coherence': 7, 'fluency': 6}, {'id': 6376, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 6377, 'relevance': 7, 'coherence': 8, 'fluency': 7}, {'id': 18316, 'relevance': 5, 'coherence': 5, 'fluency': 5}, {'id': 6378, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 6379, 'relevance': 9, 'coherence': 8, 'fluency': 9}, {'id': 8591, 'relevance': 8, 'coherence': 8, 'fluency': 7}, {'id': 15798, 'relevance': 5, 'coherence': 5, 'fluency': 5}, {'id': 8590, 'relevance': 5, 'coherence': 5, 'fluency': 5}, {'id': 8592, 'relevance': 8, 'coherence': 7, 'fluency': 8}, {'id': 8593, 'relevance': 4, 'coherence': 4, 'fluency': 5}, {'id': 8594, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 18468, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 17852, 'relevance': 5, 'coherence': 5, 'fluency': 5}, {'id': 17850, 'relevance': 9, 'coherence': 8, 'fluency': 7}, {'id': 17851, 'relevance': 6, 'coherence': 4, 'fluency': 3}, {'id': 17853, 'relevance': 10, 'coherence': 9, 'fluency': 9}, {'id': 17854, 'relevance': 9, 'coherence': 7, 'fluency': 7}, {'id': 16255, 'relevance': 7, 'coherence': 3, 'fluency': 8}, {'id': 16256, 'relevance': 7, 'coherence': 3, 'fluency': 8}, {'id': 16258, 'relevance': 7, 'coherence': 3, 'fluency': 7}, {'id': 16259, 'relevance': 2, 'coherence': 3, 'fluency': 3}, {'id': 16257, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 18444, 'relevance': 7, 'coherence': 3, 'fluency': 8}, {'id': 17320, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 17321, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 17322, 'relevance': 10, 'coherence': 8, 'fluency': 8}, {'id': 17323, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 18466, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 17324, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 18438, 'relevance': 9, 'coherence': 8, 'fluency': 8}, {'id': 12707, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 12708, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 12709, 'relevance': 7, 'coherence': 8, 'fluency': 8}, {'id': 12710, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 12711, 'relevance': 7, 'coherence': 7, 'fluency': 8}, {'id': 17160, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 17161, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 17162, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 17163, 'relevance': 10, 'coherence': 10, 'fluency': 9}, {'id': 17164, 'relevance': 9, 'coherence': 8, 'fluency': 8}, {'id': 18470, 'relevance': 8, 'coherence': 7, 'fluency': 8}, {'id': 13831, 'relevance': 10, 'coherence': 8, 'fluency': 3}, {'id': 13827, 'relevance': 10, 'coherence': 10, 'fluency': 10}, {'id': 13828, 'relevance': 3, 'coherence': 10, 'fluency': 10}, {'id': 13829, 'relevance': 6, 'coherence': 6, 'fluency': 9}, {'id': 13830, 'relevance': 3, 'coherence': 10, 'fluency': 3}, {'id': 18418, 'relevance': 3, 'coherence': 3, 'fluency': 10}, {'id': 9845, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 9846, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 9847, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 9848, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 9849, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 18487, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 16935, 'relevance': 10, 'coherence': 9, 'fluency': 8}, {'id': 16936, 'relevance': 9, 'coherence': 8, 'fluency': 8}, {'id': 16937, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 16938, 'relevance': 9, 'coherence': 9, 'fluency': 8}, {'id': 16939, 'relevance': 9, 'coherence': 8, 'fluency': 8}, {'id': 18498, 'relevance': 10, 'coherence': 8, 'fluency': 8}, {'id': 9900, 'relevance': 10, 'coherence': 10, 'fluency': 10}, {'id': 9901, 'relevance': 10, 'coherence': 10, 'fluency': 10}, {'id': 9902, 'relevance': 10, 'coherence': 10, 'fluency': 10}, {'id': 9903, 'relevance': 10, 'coherence': 10, 'fluency': 10}, {'id': 9904, 'relevance': 10, 'coherence': 10, 'fluency': 10}, {'id': 16127, 'relevance': 10, 'coherence': 10, 'fluency': 3}, {'id': 18447, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 16641, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 16643, 'relevance': 7, 'coherence': 7, 'fluency': 9}, {'id': 16644, 'relevance': 7, 'coherence': 6, 'fluency': 8}, {'id': 16642, 'relevance': 8, 'coherence': 7, 'fluency': 8}, {'id': 16640, 'relevance': 8, 'coherence': 7, 'fluency': 8}, {'id': 15695, 'relevance': 9, 'coherence': 8, 'fluency': 9}, {'id': 7070, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 7072, 'relevance': 5, 'coherence': 6, 'fluency': 6}, {'id': 7071, 'relevance': 7, 'coherence': 7, 'fluency': 8}, {'id': 7073, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 7074, 'relevance': 6, 'coherence': 7, 'fluency': 7}, {'id': 12972, 'relevance': 7, 'coherence': 6, 'fluency': 6}, {'id': 12973, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 12974, 'relevance': 7, 'coherence': 8, 'fluency': 8}, {'id': 12975, 'relevance': 8, 'coherence': 7, 'fluency': 7}, {'id': 12976, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 18486, 'relevance': 7, 'coherence': 6, 'fluency': 7}, {'id': 2843, 'relevance': 3, 'coherence': 2, 'fluency': 3}, {'id': 5110, 'relevance': 5, 'coherence': 2, 'fluency': 3}, {'id': 2841, 'relevance': 5, 'coherence': 2, 'fluency': 10}, {'id': 2842, 'relevance': 2, 'coherence': 3, 'fluency': 10}, {'id': 2844, 'relevance': 2, 'coherence': 3, 'fluency': 10}, {'id': 2845, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 7750, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 7751, 'relevance': 4, 'coherence': 5, 'fluency': 5}, {'id': 7752, 'relevance': 5, 'coherence': 5, 'fluency': 5}, {'id': 7753, 'relevance': 5, 'coherence': 5, 'fluency': 5}, {'id': 7754, 'relevance': 6, 'coherence': 6, 'fluency': 5}, {'id': 16089, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 3667, 'relevance': 3, 'coherence': 3, 'fluency': 6}, {'id': 3668, 'relevance': 3, 'coherence': 3, 'fluency': 9}, {'id': 3666, 'relevance': 3, 'coherence': 6, 'fluency': 6}, {'id': 5221, 'relevance': 9, 'coherence': 9, 'fluency': 6}, {'id': 3669, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 3670, 'relevance': 3, 'coherence': 3, 'fluency': 6}, {'id': 16153, 'relevance': 8, 'coherence': 7, 'fluency': 10}, {'id': 12786, 'relevance': 6, 'coherence': 6, 'fluency': 8}, {'id': 12782, 'relevance': 8, 'coherence': 8, 'fluency': 6}, {'id': 12783, 'relevance': 9, 'coherence': 9, 'fluency': 7}, {'id': 12784, 'relevance': 8, 'coherence': 6, 'fluency': 7}, {'id': 12785, 'relevance': 5, 'coherence': 6, 'fluency': 5}, {'id': 17221, 'relevance': 7, 'coherence': 6, 'fluency': 8}, {'id': 17222, 'relevance': 9, 'coherence': 8, 'fluency': 9}, {'id': 17223, 'relevance': 9, 'coherence': 7, 'fluency': 7}, {'id': 17224, 'relevance': 8, 'coherence': 5, 'fluency': 8}, {'id': 18365, 'relevance': 2, 'coherence': 2, 'fluency': 7}, {'id': 17220, 'relevance': 9, 'coherence': 7, 'fluency': 7}, {'id': 7307, 'relevance': 3, 'coherence': 3, 'fluency': 2}, {'id': 7305, 'relevance': 4, 'coherence': 4, 'fluency': 3}, {'id': 7306, 'relevance': 4, 'coherence': 3, 'fluency': 3}, {'id': 7308, 'relevance': 4, 'coherence': 3, 'fluency': 3}, {'id': 7309, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 12316, 'relevance': 5, 'coherence': 3, 'fluency': 3}, {'id': 18567, 'relevance': 8, 'coherence': 7, 'fluency': 8}, {'id': 9685, 'relevance': 8, 'coherence': 7, 'fluency': 8}, {'id': 9686, 'relevance': 8, 'coherence': 8, 'fluency': 6}, {'id': 9687, 'relevance': 7, 'coherence': 6, 'fluency': 8}, {'id': 9688, 'relevance': 8, 'coherence': 6, 'fluency': 8}, {'id': 9689, 'relevance': 7, 'coherence': 8, 'fluency': 7}, {'id': 7946, 'relevance': 4, 'coherence': 3, 'fluency': 2}, {'id': 7945, 'relevance': 5, 'coherence': 2, 'fluency': 4}, {'id': 7947, 'relevance': 3, 'coherence': 3, 'fluency': 4}, {'id': 16033, 'relevance': 3, 'coherence': 2, 'fluency': 2}, {'id': 7948, 'relevance': 2, 'coherence': 3, 'fluency': 3}, {'id': 7949, 'relevance': 3, 'coherence': 2, 'fluency': 3}, {'id': 18217, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 18557, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 18219, 'relevance': 4, 'coherence': 5, 'fluency': 4}, {'id': 18215, 'relevance': 8, 'coherence': 7, 'fluency': 7}, {'id': 18216, 'relevance': 10, 'coherence': 10, 'fluency': 10}, {'id': 18218, 'relevance': 7, 'coherence': 6, 'fluency': 5}, {'id': 18255, 'relevance': 8, 'coherence': 8, 'fluency': 7}, {'id': 18256, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 18257, 'relevance': 8, 'coherence': 7, 'fluency': 6}, {'id': 18258, 'relevance': 8, 'coherence': 8, 'fluency': 7}, {'id': 18259, 'relevance': 8, 'coherence': 7, 'fluency': 7}, {'id': 18544, 'relevance': 10, 'coherence': 10, 'fluency': 10}, {'id': 12532, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 12533, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 12534, 'relevance': 8, 'coherence': 8, 'fluency': 7}, {'id': 12535, 'relevance': 8, 'coherence': 7, 'fluency': 8}, {'id': 12536, 'relevance': 8, 'coherence': 7, 'fluency': 8}, {'id': 18523, 'relevance': 8, 'coherence': 7, 'fluency': 8}, {'id': 13404, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 13402, 'relevance': 3, 'coherence': 8, 'fluency': 2}, {'id': 13403, 'relevance': 8, 'coherence': 8, 'fluency': 3}, {'id': 13405, 'relevance': 4, 'coherence': 7, 'fluency': 8}, {'id': 13406, 'relevance': 3, 'coherence': 4, 'fluency': 3}, {'id': 15704, 'relevance': 3, 'coherence': 8, 'fluency': 8}, {'id': 12547, 'relevance': 6, 'coherence': 7, 'fluency': 7}, {'id': 12548, 'relevance': 6, 'coherence': 6, 'fluency': 7}, {'id': 12549, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 12550, 'relevance': 7, 'coherence': 6, 'fluency': 8}, {'id': 12551, 'relevance': 6, 'coherence': 7, 'fluency': 6}, {'id': 18633, 'relevance': 5, 'coherence': 5, 'fluency': 5}, {'id': 10876, 'relevance': 8, 'coherence': 7, 'fluency': 9}, {'id': 10877, 'relevance': 6, 'coherence': 7, 'fluency': 6}, {'id': 10878, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 10879, 'relevance': 8, 'coherence': 7, 'fluency': 9}, {'id': 10880, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 16171, 'relevance': 4, 'coherence': 5, 'fluency': 5}, {'id': 18555, 'relevance': 7, 'coherence': 6, 'fluency': 6}, {'id': 16260, 'relevance': 8, 'coherence': 6, 'fluency': 7}, {'id': 16261, 'relevance': 4, 'coherence': 5, 'fluency': 7}, {'id': 16262, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 16263, 'relevance': 9, 'coherence': 8, 'fluency': 8}, {'id': 16264, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 17925, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 17926, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 17927, 'relevance': 2, 'coherence': 2, 'fluency': 4}, {'id': 17928, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 18501, 'relevance': 10, 'coherence': 10, 'fluency': 10}, {'id': 17929, 'relevance': 8, 'coherence': 7, 'fluency': 5}, {'id': 6935, 'relevance': 1, 'coherence': 1, 'fluency': 1}, {'id': 6937, 'relevance': 8, 'coherence': 6, 'fluency': 10}, {'id': 6936, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 6938, 'relevance': 10, 'coherence': 8, 'fluency': 10}, {'id': 6939, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 15649, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 18295, 'relevance': 9, 'coherence': 9, 'fluency': 8}, {'id': 16700, 'relevance': 7, 'coherence': 8, 'fluency': 7}, {'id': 16701, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 16702, 'relevance': 7, 'coherence': 6, 'fluency': 6}, {'id': 16703, 'relevance': 8, 'coherence': 7, 'fluency': 8}, {'id': 16704, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 9295, 'relevance': 1, 'coherence': 1, 'fluency': 1}, {'id': 9296, 'relevance': 3, 'coherence': 2, 'fluency': 3}, {'id': 9297, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 9298, 'relevance': 3, 'coherence': 3, 'fluency': 2}, {'id': 9299, 'relevance': 3, 'coherence': 1, 'fluency': 2}, {'id': 18608, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 7470, 'relevance': 2, 'coherence': 2, 'fluency': 1}, {'id': 7471, 'relevance': 2, 'coherence': 3, 'fluency': 3}, {'id': 7472, 'relevance': 2, 'coherence': 2, 'fluency': 3}, {'id': 7473, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 7474, 'relevance': 2, 'coherence': 2, 'fluency': 1}, {'id': 18628, 'relevance': 2, 'coherence': 2, 'fluency': 1}, {'id': 15684, 'relevance': 8, 'coherence': 8, 'fluency': 6}, {'id': 10521, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 10522, 'relevance': 8, 'coherence': 8, 'fluency': 10}, {'id': 10523, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 10524, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 10525, 'relevance': 8, 'coherence': 6, 'fluency': 6}, {'id': 9561, 'relevance': 4, 'coherence': 3, 'fluency': 4}, {'id': 9562, 'relevance': 8, 'coherence': 6, 'fluency': 8}, {'id': 9560, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 9563, 'relevance': 8, 'coherence': 7, 'fluency': 8}, {'id': 9564, 'relevance': 7, 'coherence': 8, 'fluency': 8}, {'id': 16104, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 18469, 'relevance': 8, 'coherence': 6, 'fluency': 8}, {'id': 17604, 'relevance': 8, 'coherence': 7, 'fluency': 8}, {'id': 17600, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 17601, 'relevance': 8, 'coherence': 7, 'fluency': 8}, {'id': 17602, 'relevance': 8, 'coherence': 6, 'fluency': 8}, {'id': 17603, 'relevance': 8, 'coherence': 7, 'fluency': 7}, {'id': 18631, 'relevance': 4, 'coherence': 2, 'fluency': 3}, {'id': 6265, 'relevance': 1, 'coherence': 2, 'fluency': 2}, {'id': 6266, 'relevance': 3, 'coherence': 3, 'fluency': 4}, {'id': 6267, 'relevance': 3, 'coherence': 2, 'fluency': 2}, {'id': 6268, 'relevance': 3, 'coherence': 2, 'fluency': 1}, {'id': 6269, 'relevance': 3, 'coherence': 4, 'fluency': 4}, {'id': 15899, 'relevance': 3, 'coherence': 6, 'fluency': 6}, {'id': 14309, 'relevance': 6, 'coherence': 5, 'fluency': 6}, {'id': 14307, 'relevance': 8, 'coherence': 5, 'fluency': 9}, {'id': 14308, 'relevance': 9, 'coherence': 10, 'fluency': 5}, {'id': 14310, 'relevance': 8, 'coherence': 2, 'fluency': 5}, {'id': 14311, 'relevance': 7, 'coherence': 6, 'fluency': 5}, {'id': 16048, 'relevance': 10, 'coherence': 9, 'fluency': 10}, {'id': 11911, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 11912, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 11913, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 11914, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 11915, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 18354, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 18253, 'relevance': 7, 'coherence': 6, 'fluency': 6}, {'id': 18254, 'relevance': 8, 'coherence': 7, 'fluency': 6}, {'id': 18250, 'relevance': 7, 'coherence': 6, 'fluency': 7}, {'id': 18251, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 18252, 'relevance': 8, 'coherence': 6, 'fluency': 6}, {'id': 17905, 'relevance': 7, 'coherence': 6, 'fluency': 7}, {'id': 17906, 'relevance': 7, 'coherence': 8, 'fluency': 7}, {'id': 17907, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 17908, 'relevance': 8, 'coherence': 8, 'fluency': 7}, {'id': 18427, 'relevance': 8, 'coherence': 7, 'fluency': 8}, {'id': 17909, 'relevance': 8, 'coherence': 6, 'fluency': 7}, {'id': 6187, 'relevance': 3, 'coherence': 1, 'fluency': 2}, {'id': 18419, 'relevance': 3, 'coherence': 3, 'fluency': 4}, {'id': 6185, 'relevance': 1, 'coherence': 2, 'fluency': 1}, {'id': 6186, 'relevance': 4, 'coherence': 1, 'fluency': 3}, {'id': 6188, 'relevance': 2, 'coherence': 2, 'fluency': 3}, {'id': 6189, 'relevance': 3, 'coherence': 1, 'fluency': 3}, {'id': 7610, 'relevance': 3, 'coherence': 3, 'fluency': 2}, {'id': 7611, 'relevance': 3, 'coherence': 3, 'fluency': 1}, {'id': 7612, 'relevance': 2, 'coherence': 1, 'fluency': 3}, {'id': 7613, 'relevance': 1, 'coherence': 1, 'fluency': 2}, {'id': 18395, 'relevance': 1, 'coherence': 2, 'fluency': 2}, {'id': 7614, 'relevance': 1, 'coherence': 1, 'fluency': 2}, {'id': 6418, 'relevance': 0, 'coherence': 0, 'fluency': 0}, {'id': 15780, 'relevance': 1, 'coherence': 1, 'fluency': 1}, {'id': 6415, 'relevance': 3, 'coherence': 4, 'fluency': 3}, {'id': 6416, 'relevance': 3, 'coherence': 2, 'fluency': 2}, {'id': 6417, 'relevance': 3, 'coherence': 1, 'fluency': 2}, {'id': 6419, 'relevance': 1, 'coherence': 3, 'fluency': 1}, {'id': 6160, 'relevance': 5, 'coherence': 6, 'fluency': 5}, {'id': 6161, 'relevance': 5, 'coherence': 5, 'fluency': 5}, {'id': 6162, 'relevance': 6, 'coherence': 7, 'fluency': 5}, {'id': 6163, 'relevance': 5, 'coherence': 5, 'fluency': 5}, {'id': 6164, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 18407, 'relevance': 5, 'coherence': 5, 'fluency': 5}, {'id': 14890, 'relevance': 3, 'coherence': 3, 'fluency': 2}, {'id': 14891, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 16192, 'relevance': 10, 'coherence': 10, 'fluency': 10}, {'id': 14887, 'relevance': 10, 'coherence': 10, 'fluency': 10}, {'id': 14888, 'relevance': 3, 'coherence': 2, 'fluency': 3}, {'id': 14889, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 13757, 'relevance': 1, 'coherence': 2, 'fluency': 1}, {'id': 13758, 'relevance': 1, 'coherence': 3, 'fluency': 2}, {'id': 13759, 'relevance': 2, 'coherence': 2, 'fluency': 1}, {'id': 13761, 'relevance': 2, 'coherence': 3, 'fluency': 3}, {'id': 16023, 'relevance': 1, 'coherence': 2, 'fluency': 3}, {'id': 13760, 'relevance': 3, 'coherence': 1, 'fluency': 1}, {'id': 18352, 'relevance': 8, 'coherence': 5, 'fluency': 5}, {'id': 16955, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 16956, 'relevance': 10, 'coherence': 10, 'fluency': 10}, {'id': 16957, 'relevance': 10, 'coherence': 8, 'fluency': 8}, {'id': 16958, 'relevance': 10, 'coherence': 9, 'fluency': 9}, {'id': 16959, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 18235, 'relevance': 10, 'coherence': 8, 'fluency': 8}, {'id': 18236, 'relevance': 9, 'coherence': 8, 'fluency': 8}, {'id': 18237, 'relevance': 8, 'coherence': 6, 'fluency': 7}, {'id': 18238, 'relevance': 9, 'coherence': 8, 'fluency': 8}, {'id': 18559, 'relevance': 8, 'coherence': 6, 'fluency': 7}, {'id': 18239, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 15917, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 14827, 'relevance': 6, 'coherence': 6, 'fluency': 5}, {'id': 14828, 'relevance': 8, 'coherence': 9, 'fluency': 8}, {'id': 14829, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 14830, 'relevance': 5, 'coherence': 6, 'fluency': 6}, {'id': 14831, 'relevance': 8, 'coherence': 6, 'fluency': 7}, {'id': 18070, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 18071, 'relevance': 8, 'coherence': 4, 'fluency': 6}, {'id': 18072, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 18073, 'relevance': 8, 'coherence': 6, 'fluency': 6}, {'id': 18074, 'relevance': 10, 'coherence': 8, 'fluency': 8}, {'id': 18778, 'relevance': 8, 'coherence': 6, 'fluency': 6}, {'id': 9539, 'relevance': 0, 'coherence': 0, 'fluency': 0}, {'id': 12312, 'relevance': 0, 'coherence': 0, 'fluency': 0}, {'id': 9535, 'relevance': 1, 'coherence': 1, 'fluency': 1}, {'id': 9536, 'relevance': 2, 'coherence': 2, 'fluency': 1}, {'id': 9537, 'relevance': 2, 'coherence': 2, 'fluency': 1}, {'id': 9538, 'relevance': 1, 'coherence': 3, 'fluency': 2}, {'id': 18775, 'relevance': 7, 'coherence': 7, 'fluency': 8}, {'id': 5889, 'relevance': 7, 'coherence': 7, 'fluency': 8}, {'id': 5885, 'relevance': 7, 'coherence': 7, 'fluency': 8}, {'id': 5886, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 5887, 'relevance': 9, 'coherence': 8, 'fluency': 9}, {'id': 5888, 'relevance': 8, 'coherence': 7, 'fluency': 7}, {'id': 16183, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 14317, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 14318, 'relevance': 2, 'coherence': 2, 'fluency': 2}, {'id': 14320, 'relevance': 10, 'coherence': 9, 'fluency': 10}, {'id': 14321, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 14319, 'relevance': 3, 'coherence': 2, 'fluency': 3}, {'id': 12652, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 12653, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 12654, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 12655, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 12656, 'relevance': 8, 'coherence': 8, 'fluency': 10}, {'id': 18669, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 15904, 'relevance': 6, 'coherence': 6, 'fluency': 5}, {'id': 14904, 'relevance': 6, 'coherence': 5, 'fluency': 6}, {'id': 14902, 'relevance': 8, 'coherence': 8, 'fluency': 9}, {'id': 14903, 'relevance': 7, 'coherence': 6, 'fluency': 6}, {'id': 14905, 'relevance': 8, 'coherence': 7, 'fluency': 7}, {'id': 14906, 'relevance': 8, 'coherence': 7, 'fluency': 8}, {'id': 16268, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 16265, 'relevance': 4, 'coherence': 4, 'fluency': 5}, {'id': 16266, 'relevance': 5, 'coherence': 5, 'fluency': 5}, {'id': 16267, 'relevance': 9, 'coherence': 8, 'fluency': 8}, {'id': 18491, 'relevance': 10, 'coherence': 9, 'fluency': 9}, {'id': 16269, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 8270, 'relevance': 5, 'coherence': 5, 'fluency': 5}, {'id': 8271, 'relevance': 5, 'coherence': 7, 'fluency': 5}, {'id': 8272, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 8273, 'relevance': 5, 'coherence': 5, 'fluency': 5}, {'id': 8274, 'relevance': 5, 'coherence': 5, 'fluency': 5}, {'id': 18751, 'relevance': 4, 'coherence': 6, 'fluency': 5}, {'id': 18355, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 17890, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 17891, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 17892, 'relevance': 7, 'coherence': 6, 'fluency': 6}, {'id': 17893, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 17894, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 15645, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 7186, 'relevance': 7, 'coherence': 6, 'fluency': 7}, {'id': 7185, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 7187, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 7188, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 7189, 'relevance': 7, 'coherence': 7, 'fluency': 7}, {'id': 17285, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 17286, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 17287, 'relevance': 8, 'coherence': 6, 'fluency': 5}, {'id': 17288, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 18300, 'relevance': 8, 'coherence': 6, 'fluency': 7}, {'id': 17289, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 16565, 'relevance': 9, 'coherence': 8, 'fluency': 8}, {'id': 16566, 'relevance': 8, 'coherence': 8, 'fluency': 9}, {'id': 16567, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 16568, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 16569, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 18568, 'relevance': 9, 'coherence': 8, 'fluency': 7}, {'id': 6770, 'relevance': 8, 'coherence': 9, 'fluency': 8}, {'id': 6771, 'relevance': 8, 'coherence': 7, 'fluency': 8}, {'id': 6772, 'relevance': 7, 'coherence': 8, 'fluency': 8}, {'id': 6773, 'relevance': 8, 'coherence': 8, 'fluency': 9}, {'id': 6774, 'relevance': 8, 'coherence': 8, 'fluency': 9}, {'id': 18714, 'relevance': 8, 'coherence': 7, 'fluency': 8}, {'id': 16049, 'relevance': 8, 'coherence': 10, 'fluency': 8}, {'id': 11116, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 11117, 'relevance': 8, 'coherence': 6, 'fluency': 8}, {'id': 11118, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 11119, 'relevance': 8, 'coherence': 4, 'fluency': 8}, {'id': 11120, 'relevance': 8, 'coherence': 6, 'fluency': 8}, {'id': 7420, 'relevance': 7, 'coherence': 7, 'fluency': 6}, {'id': 7421, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 7422, 'relevance': 5, 'coherence': 5, 'fluency': 5}, {'id': 7423, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 7424, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 18721, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 22127, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 19279, 'relevance': 9, 'coherence': 9, 'fluency': 9}, {'id': 19280, 'relevance': 3, 'coherence': 4, 'fluency': 4}, {'id': 19281, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 19282, 'relevance': 8, 'coherence': 7, 'fluency': 7}, {'id': 19283, 'relevance': 8, 'coherence': 6, 'fluency': 6}, {'id': 17134, 'relevance': 8, 'coherence': 8, 'fluency': 8}, {'id': 17130, 'relevance': 4, 'coherence': 4, 'fluency': 5}, {'id': 17131, 'relevance': 8, 'coherence': 3, 'fluency': 3}, {'id': 17132, 'relevance': 7, 'coherence': 6, 'fluency': 6}, {'id': 17133, 'relevance': 4, 'coherence': 4, 'fluency': 4}, {'id': 18665, 'relevance': 6, 'coherence': 6, 'fluency': 6}, {'id': 22131, 'relevance': 2, 'coherence': 3, 'fluency': 2}, {'id': 20554, 'relevance': 3, 'coherence': 2, 'fluency': 2}, {'id': 20555, 'relevance': 3, 'coherence': 3, 'fluency': 3}, {'id': 20556, 'relevance': 2, 'coherence': 4, 'fluency': 2}, {'id': 20557, 'relevance': 3, 'coherence': 4, 'fluency': 4}, {'id': 20558, 'relevance': 3, 'coherence': 2, 'fluency': 2}]

import json

from app.status import (
	HTTP_200_OK,
	HTTP_201_CREATED,
	HTTP_204_NO_CONTENT,
	HTTP_400_BAD_REQUEST,
	HTTP_404_NOT_FOUND,
	HTTP_409_CONFLICT,
)
from flask import Blueprint, request, send_file
from flask.json import jsonify
import pandas as pd
from flask_jwt_extended import get_jwt_identity, jwt_required, verify_jwt_in_request
from app.models import Question, db, User, Answer
import datetime
import random
import os
from os.path import join, dirname, realpath
from io import StringIO
from google.cloud import storage

from sqlalchemy import func, or_, and_, not_, text
from app.helper import admin_required

UPLOADS_PATH = join(dirname(realpath(__file__)), "static/audio_uploads")
DATASET_PATH = join(dirname(realpath(__file__)), "static/dataset")

questions = Blueprint("questions", __name__, url_prefix="/api/v1/questions")

def get_audio_file_content(file_path):
	# file_path = os.path.join(UPLOADS_PATH, filename)
	return send_file(file_path, as_attachment=True)



def format_question(question, language):
	return {
		"id": question.id,
		"sentence": question.sentence,
		"language": question.language,
		"created_at": question.created_at.strftime("%Y-%m-%d %H:%M:%S"),
		"topics": question.topic,
		"sub_topic": question.sub_topic,
		"category": question.category,
		"animal_crop": question.animal_crop,
		"location": question.location,
		"question_language": language,
		"filename": question.filename,
	}

def jsonify_question(question):
	return {
		"id": question.id,
		"sentence": question.sentence,
		"language": question.language,
		"created_at": question.created_at.strftime("%Y-%m-%d %H:%M:%S"),
		"topics": question.topic,
		"sub_topic": question.sub_topic,
		"category": question.category,
		"animal_crop": question.animal_crop,
		"location": question.location,
		"filename": question.filename,
		"reviewed": question.reviewed,
		"answered": question.answered
	}

def file_name(file):
	name = file.filename
	file_name, file_extension = os.path.splitext(name)
	return file_name, file_extension

def chanelle(value):
	if int(value) == 6:
		return 5
	try:
		return int(value)
	except ValueError:
		return 1

@questions.route("/", methods=["POST", "GET"])
@jwt_required()
def handle_questions():
	def process_single_question(question_data, current_user):
		sentence = question_data.get("sentence", "")
		language = question_data.get("language", "")
		topic = question_data.get("topic", "")
		sub_topic = question_data.get("sub_topics", "")
		category = question_data.get("category", "")
		animal_crop = question_data.get("sub_category", "")
		location = question_data.get("location", "")
		today = datetime.date.today()

		if language not in ["English", "Luganda", "Runyankole"]:
			return (
				jsonify({"error": "Invalid language selection"}),
				HTTP_400_BAD_REQUEST,
			)

		if not sentence or not language:
			return (
				jsonify(
					{
						"error": "Both sentence and language must be provided for each question"
					}
				),
				HTTP_400_BAD_REQUEST,
			)

		elif Question.query.filter_by(sentence=sentence).first():
			return (
				jsonify({"error": "This question already exists"}),
				HTTP_409_CONFLICT,
			)
		else:
			question = Question(
				sentence=sentence,
				language=language,
				user_id=current_user,
				topic=topic,
				category=category,
				animal_crop=animal_crop,
				location=location,
				sub_topic=sub_topic,
			)
			db.session.add(question)
			db.session.flush()

			num_questions = Question.query.filter_by(user_id=current_user).count()
			today = datetime.date.today()
			questions = (
				Question.query.filter_by(user_id=current_user)
				.filter(func.date(Question.created_at) == today)
				.all()
			)
			todaysQuestions = []
			for question in questions:
				todaysQuestions.append(
					{
						"id": question.id,
						"sentence": question.sentence,
						"language": question.language,
						"created_at": question.created_at,
						"topics": question.topic,
						"sub_topic": question.sub_topic,
						"category": question.category,
						"animal_crop": question.animal_crop,
						"location": question.location,
					}
				)

			return {
				"num_questions": num_questions,
				"questions": todaysQuestions,
			}, HTTP_201_CREATED

	current_user = get_jwt_identity()

	if request.method == "POST":
		data = request.get_json()

		if not data:
			return (
				jsonify({"error": "Invalid or empty JSON data provided"}),
				HTTP_400_BAD_REQUEST,
			)

		if isinstance(data, list): 
			results = []
			for question_data in data:
				result = process_single_question(question_data, current_user)
				results.append(result)
			db.session.commit()
			return jsonify(results), HTTP_201_CREATED
		else:  # If it's a single question
			result = process_single_question(data, current_user)
			db.session.commit()
			return result

	else:
		user = User.query.filter_by(id=current_user).first()
		if user:
			questions = user.questions

			returned_data = []

			if not questions:
				return jsonify({"error": "No data yet"}), HTTP_204_NO_CONTENT

			for question in questions:
				returned_data.append(
					{
						"id": question.id,
						"sentence": question.sentence,
						"language": question.language,
						"created_at": question.created_at,
						"topics": question.topic,
						"sub_topic": question.sub_topic,
						"category": question.category,
						"animal_crop": question.animal_crop,
						"location": question.location,
					}
				)

			return jsonify(returned_data), HTTP_200_OK
		else:
			return jsonify({"error": "User not found"}), HTTP_404_NOT_FOUND


@questions.route("/upload_question", methods=["POST"])
@jwt_required()
def upload_question():
	if "audio" not in request.files:
		return jsonify({"error": "No audio file provided"}), HTTP_400_BAD_REQUEST

	language = request.form.get("language")
	topic = request.form.get("topic", "")
	sub_topic = request.form.get("sub_topics", "")
	category = request.form.get("category", "")
	animal_crop = request.form.get("sub_category", "")
	location = request.form.get("location", "")

	audio = request.files["audio"]

	if audio:
		filename = os.path.join("static", "audio_uploads", audio.filename)
		if os.path.exists(filename):
			return jsonify({"Error": "File with same name already exists"})
		audio.save(filename)

	current_user = get_jwt_identity()
	question = Question(
		language=language,
		user_id=current_user,
		topic=topic,
		sub_topic=sub_topic,
		filename=filename,
		category=category,
		animal_crop=animal_crop,
		location=location,
	)

	db.session.add(question)
	db.session.flush()

	num_questions = Question.query.filter_by(user_id=current_user).count()
	today = datetime.date.today()
	questions = (
		Question.query.filter_by(user_id=current_user)
		.filter(func.date(Question.created_at) == today)
		.all()
	)
	todaysQuestions = []
	for question in questions:
		todaysQuestions.append(
			{
				"id": question.id,
				"sentence": question.sentence,
				"language": question.language,
				"created_at": question.created_at,
				"topics": question.topic,
				"sub_topic": question.sub_topic,
				"category": question.category,
				"animal_crop": question.animal_crop,
				"location": question.location,
				"filename": question.filename
			}
		)

	return {
		"num_questions": num_questions,
		"questions": todaysQuestions,
	}, HTTP_201_CREATED


@questions.route("/offline_upload", methods=["POST"])
@jwt_required()
def offline_upload():
	if "file" not in request.files:
		return jsonify({"error": "No metadata file provided"}), HTTP_400_BAD_REQUEST

	if "files" not in request.files:
		return jsonify({"error": "No audio files provided"}), HTTP_400_BAD_REQUEST

	metadata_file = request.files.get("file")
	audio_files = request.files.getlist("files")
	metadata = json.loads(metadata_file.read().decode("utf-8"))

	if not audio_files:
		return jsonify({"error": "No audio files provided"}), HTTP_400_BAD_REQUEST

	if not metadata:
		return jsonify({"error": "Metadata file not provided"}), HTTP_400_BAD_REQUEST

	current_user = get_jwt_identity()

	questions = []
	dup_count = 0
	duplicates = []

	for obj in metadata:
		audio_filename = obj['audio_filePath'].rsplit('.', 1)[0]
		
		for audio in audio_files:
			au  =  file_name(audio)[0]
			
			if audio_filename == au:
				
				filename = os.path.join("static", "audio_uploads", obj["audio_filename"])

				if os.path.exists(filename):
					dup_count += 1
					duplicates.append({"filename": filename})
					return (
						jsonify({"error": "File with the same name already exists"}),
						HTTP_400_BAD_REQUEST,
					)
				audio.save(filename) 		

				if obj:
					question_data = {
						"language": obj.get("language"),
						"topic": obj.get("topic", ""),
						"sub_topic": obj.get("sub_topics", ""),
						"category": obj.get("category", ""),
						"animal_crop": obj.get("sub_category", ""),
						"location": obj.get("location", ""),
						"user_id": current_user,
						"filename": filename,
					}

					question = Question(**question_data)
					questions.append(question)
				else:
					return (
						jsonify(
							{"error": f"No metadata found for audio file: {audio.filename}"}
						),
						HTTP_400_BAD_REQUEST,
					)

	db.session.add_all(questions)
	db.session.commit()

	num_questions = Question.query.filter_by(user_id=current_user).count()
	return (
		jsonify(
			{
				"num_questions": num_questions,
				"duplicate_questions": dup_count,
				"duplicates": duplicates,
			}
		),
		HTTP_200_OK,
	)


@questions.route("/file_upload/", methods=["POST"])
@jwt_required()
def upload_json_file():
	if request.method == "POST":
		file_json = request.files.get("file")
		json_data = json.load(file_json)

		current_user = get_jwt_identity()
		dup_count = 0
		duplicates = []

		for obj in json_data:
			sentence = obj["sentence"]
			language = obj["language"]
			topic = obj.get("topic")
			sub_topic = obj.get("sub_topics")
			category = obj.get("category")
			animal_crop = obj.get("sub_category")
			location = obj.get("location")

			if Question.query.filter_by(sentence=sentence).first():
				dup_count += 1
				duplicates.append({"sentence": sentence})
			else:
				question = Question(
					sentence=sentence,
					language=language,
					user_id=current_user,
					topic=topic,
					sub_topic=sub_topic,
					category=category,
					animal_crop=animal_crop,
					location=location,
				)
				db.session.add(question)
				db.session.commit()

		num_questions = Question.query.filter_by(user_id=current_user).count()

		return (
			jsonify(
				{
					"num_questions": num_questions,
					"duplicate_questions": dup_count,
					"duplicates": duplicates,
				}
			),
			HTTP_200_OK,
		)


@questions.get("/<int:id>")
@jwt_required()
def get_question(id):
	current_user = get_jwt_identity()

	question = Question.query.filter_by(user_id=current_user, id=id).first()

	if not question:
		return jsonify({"message": "Question not found"}), HTTP_404_NOT_FOUND

	return (
		jsonify(
			{
				"id": question.id,
				"language": question.language,
				"sentence": question.sentence,
				"created_at": question.created_at,
				"category": question.category,
				"animal_crop": question.animal_crop,
				"location": question.location,
			}
		),
		HTTP_200_OK,
	)

@jwt_required()
@questions.get('/delete-questions')
def delete_questions():
	try:
		questions_to_delete = Question.query.filter(Question.rephrased == "actual", Question.reviewed != True).all()
		
		# for question in questions_to_delete:
		#		Answer.query.filter_by(question_id=question.id).delete()

		# num_deleted = Question.query.filter(Question.rephrased == "actual", Question.reviewed != True).delete()
		num_deleted = len(questions_to_delete)

		db.session.commit()
		return jsonify({'message': f'{num_deleted} questions and associated answers deleted successfully'})
	except Exception as e:
		db.session.rollback()
		return jsonify({'error': 'An error occurred while deleting questions and answers'})


@jwt_required()
@questions.get("/displayall")
def display_questions():
	verify_jwt_in_request()
	curre = get_jwt_identity()
	isadmin = User.query.get(curre)
	page = request.args.get('page', 1, type=int)
	per_page = request.args.get('per_page', 100, type=int)
	questions = Question.query.filter(
		(Question.user_id != isadmin.id)
	).paginate(page=page, per_page=per_page, error_out=False)

	if not questions:
		return jsonify({"message": "No questions yet."}), HTTP_204_NO_CONTENT

	returned_data = []

	for question in questions:
		user = User.query.get(question.user_id)  # Get the user who asked the question
		if user:
			user_name = f"{user.firstname} {user.lastname}"

		returned_data.append(
			{
				"id": question.id,
				"sentence": question.sentence,
				"language": question.language,
				"created_at": question.created_at.strftime("%Y-%m-%d %H:%M:%S"),
				"topics": question.topic,
				"sub_topic": question.sub_topic,
				"category": question.category,
				"animal_crop": question.animal_crop,
				"location": question.location,
				"audio": question.filename,
				"user_name": user_name,
			}
		)

	return jsonify(returned_data), HTTP_200_OK


@jwt_required()
@questions.get("/all")
def get_questions():
	current_user = get_jwt_identity()
	isadmin = User.query.get(current_user)
	questions = Question.query.filter(
		(Question.user_id != isadmin.id)
	).all()

	if not questions:
		return jsonify({"message": "No questions yet."}), HTTP_204_NO_CONTENT

	returned_data = []

	for question in questions:
		user = User.query.get(question.user_id)
		if user:
			user_name = f"{user.firstname} {user.lastname}"

		returned_data.append(
			{
				"id": question.id,
				"sentence": question.sentence,
				"language": question.language,
				"created_at": question.created_at.strftime("%Y-%m-%d %H:%M:%S"),
				"topics": question.topic,
				"sub_topic": question.sub_topic,
				"category": question.category,
				"animal_crop": question.animal_crop,
				"location": question.location,
				"audio": question.filename,
				"user_name": user_name,
			}
		)

	return jsonify(returned_data), HTTP_200_OK



@jwt_required()
@questions.get("/download")
def download_questions():
	verify_jwt_in_request()
	user_id = get_jwt_identity()
	isadmin = User.query.get(user_id)
	start_date_str = request.args.get('start_date')
	
	if start_date_str:
		try:
			start_date = datetime.datetime.strptime(start_date_str, '%Y-%m-%d')
			questions = Question.query.filter(
				(Question.user_id != isadmin.id) &
				(Question.created_at >= start_date)
			).all()
		except ValueError:
			return jsonify({"message": "Invalid start_date format. Use YYYY-MM-DD."}), HTTP_400_BAD_REQUEST
	else:
		questions = Question.query.filter(
			(Question.rephrased != "actual")
		).all()

	if not questions:
		return jsonify({"message": "No questions yet."}), HTTP_204_NO_CONTENT

	returned_data = []

	for question in questions:
		user = User.query.get(question.user_id)  # Get the user who asked the question
		user_name = None
		if user:
			user_name = f"{user.firstname} {user.lastname}"

		returned_data.append(
			{
				"id": question.id,
				"sentence": question.sentence,
				"language": question.language,
				"created_at": question.created_at.strftime("%Y-%m-%d %H:%M:%S"),
				"topics": question.topic,
				"sub_topic": question.sub_topic,
				"category": question.category,
				"animal_crop": question.animal_crop,
				"location": question.location,
				"audio": question.filename,
				"user_name": user_name,
			}
		)
	return jsonify(returned_data), HTTP_200_OK

@jwt_required()
@questions.get("/myqns")
def get_my_questions():
	questions = Question.query.filter(
		(Question.rephrased == "actual")
	).all()

	if not questions:
		return jsonify({"message": "No questions yet."}), HTTP_204_NO_CONTENT

	returned_data = []

	for question in questions:
		user = User.query.get(question.user_id)
		if user:
			user_name = f"{user.firstname} {user.lastname}"

		returned_data.append(
			{
				"id": question.id,
				"sentence": question.sentence,
				"language": question.language,
				"created_at": question.created_at.strftime("%Y-%m-%d %H:%M:%S"),
				"topics": question.topic,
				"sub_topic": question.sub_topic,
				"category": question.category,
				"animal_crop": question.animal_crop,
				"location": question.location,
				"user_name": user_name,
				"reviewed":question.reviewed,
				"rephrased": question.rephrased
			}
		)

	return jsonify(returned_data), HTTP_200_OK

@jwt_required()
@questions.get("/top_users")
def top_users_with_most_questions():
	users_with_most_questions = (
		User.query.join(Question, User.id == Question.user_id)
		.group_by(User.id)
		.order_by(db.func.count(Question.id).desc())
		.all()
	)
	top_users_data = []
	for user in users_with_most_questions:
		top_users_data.append(
			{
				"user_id": user.id,
				"location": user.location,
				"firstname": user.firstname,
				"lastname": user.lastname,
				"username": user.username,
				"phone_number": user.phone_number,
				"total_questions": len(user.questions),
			}
		)

	return jsonify(top_users_data), HTTP_200_OK


@jwt_required()
@questions.get("/stats")
# @admin_required
def list_questions():
	verify_jwt_in_request()
	current_user = get_jwt_identity()
	isadmin = User.query.get(current_user)
	all_questions = Question.query.filter(
		(Question.user_id != isadmin.id)
	).all()
	
	#     all_questions = db.sessionQuestion).all()
	total_questions = len(all_questions)
	questions_per_language = (
		db.session.query(Question.language, func.count(Question.id))
		.filter((Question.user_id != isadmin.id))
		.group_by(Question.language)
		.all()
	)
	
	audio_questions = Question.query.filter(Question.filename.isnot(None)).all()

	average_daily_questions = total_questions / (
		Question.query.filter(
			(Question.rephrased != "actual"),
			(Question.user_id != isadmin.id)
			& (Question.created_at >= datetime.date.today())
		).count()
		or 1
	)

	one_week_ago = datetime.date.today() - datetime.timedelta(weeks=1)
	average_weekly_questions = total_questions / (
		Question.query.filter(
			(Question.rephrased != "actual"),
			(Question.user_id != isadmin.id)
			& (Question.created_at >= one_week_ago)
		).count()
		or 1
	)

	#  Calculate average questions per user
	total_users = User.query.count()
	average_questions_per_user = total_questions / (total_users or 1)
	
	plant_question_count = Question.query.filter(
		(Question.user_id != isadmin.id)
		& (func.lower(Question.category) == "crop")
	).count()

	animal_question_count = Question.query.filter(
		(Question.user_id != isadmin.id)
		& (func.lower(Question.category) == "animal")
	).count()

	response_data = {
		"total_questions": total_questions,
		"questions_per_language": [
			{"language": lang, "count": count} for lang, count in questions_per_language
		],
		"average_daily_questions": round(average_daily_questions, 2),
		"average_weekly_questions": round(average_weekly_questions, 2),
		"average_questions_per_user": round(average_questions_per_user, 2),
		"plant_category": plant_question_count,
		"animal_category": animal_question_count,
		"audios": len(audio_questions),
		"questions": [
			{
				"id": question.id,
				"topics": question.topic,
				"sub_topic": question.sub_topic,
				"sentence": question.sentence,
				"language": question.language,
				"created_at": question.created_at,
				"category": question.category,
				"animal_crop": question.animal_crop,
				"location": question.location,
			}
			for question in all_questions
		],
	}

	return jsonify(response_data), HTTP_200_OK


@questions.route("/random_question", methods=["GET"])
@jwt_required()
def random_question_and_add_answer():
	user_id = get_jwt_identity()
	random_question = (
		Question.query.filter(~Question.answers.any(Answer.source == "expert"))
		.order_by(db.func.random())
		.first()
	)

	if random_question:
		question_data = {
			"id": random_question.id,
			"sentence": random_question.sentence,
			"language": random_question.language,
			"created_at": random_question.created_at.strftime("%Y-%m-%d %H:%M:%S"),
			"topics": random_question.topic,
			"sub_topic": random_question.sub_topic,
			"category": random_question.category,
			"animal_crop": random_question.animal_crop,
			"location": random_question.location,
		}
		return jsonify(question_data), HTTP_200_OK
	else:
		return jsonify({"message": "No questions available."}), HTTP_404_NOT_FOUND


@questions.route("/main_question_review", methods=["POST"])
@jwt_required()
def main_question_review():

	sub_category_map = {
    "poultry": ["chicken", "ducks", "guinea fowls", "turkeys"],
    "vegetables":  [
			"tomatoes", "carrots", "onions", "mushrooms", "eggplant", "beetroot",
			"doodo", "spinach", "cucumbers", "avocado", "cabbage", "nakati", "ginger",
			"green pepper", "garlic", "okra", "lettuce", "malakwang", "pepper", "sukuma wiiki",
			"kale", "hubiscus", "crops", "crop"
		],
		"cattle": ["cattle", "goat", "goats", "sheep"],
		"fish": ["fish", 'Fish'],
		"banana": ["banana", "bananas", "crop", "crops"],
		"fruits": ["watermelon", "pineapple", "mango", "sugarcane", "orange", "avocado", "passion fruit", "jack fruit", "paw paw", "guava", "lemon"],
		"cereals": ["maize", "sorghum", "millet", "rice", "wheat", "sim sim", "sesame"],
		"legumes": [ "soya beans", "beans", "peas", "groundnuts", "Gnuts", "ground nuts"],
		"piggery": ["pigs", 'animal', 'animals']
  }

	data = request.get_json()
	
	category = data.get("category", None)
	language = data.get("language", None)
	sub_category = data.get("sub_category", None)
	new_category = data.get("new_category", None)

	filters = []

	expert_id = get_jwt_identity()

	category_filter = func.lower(Question.category) == category
	answers_count = Answer.query.filter_by(user_id=expert_id).count()
	sub_categories = [sc.strip().lower() for sc in new_category.split(",")]

	if len(sub_categories) >= 3 and answers_count >= 350:
		return jsonify({"message":"You have answered enough questions. START ranking."}), HTTP_200_OK
	elif len(sub_categories) < 3 and answers_count >= 250:
		return jsonify({"message":"You have answered enough questions. START ranking."}), HTTP_200_OK
	else:
		if language:
			languages = [lang.strip().lower() for lang in language.split(",")]
			language_filter = func.lower(Question.language).in_(languages)
			filters.append(language_filter)

		if sub_category:
			sub_category_filters = []
			
			for sub_category_name in sub_categories:
				sub_category_list = sub_category_map.get(sub_category_name)
				if sub_category_list:
					sub_category_filters.append( func.lower(Question.animal_crop).in_(sub_category_list))
				else:
					sub_category_filters.append(func.lower(Question.animal_crop) == sub_category_name)
			
			if sub_category_filters:
				filters.append(or_(*sub_category_filters))

	matching_questions = (
		Question.query.filter(Question.rephrased == "actual", Question.answered.is_(False), *filters)
		.all()
	)

	if matching_questions:
		random_question = random.sample(matching_questions, 1)[0]
		questions_data = format_question(random_question, "Any Language")
		return jsonify([questions_data]), HTTP_200_OK
	else:
		return jsonify({"message": "No questions available."}), HTTP_404_NOT_FOUND


@jwt_required()
@questions.route("/main_question_answer", methods=["POST"])
def main_question_answer():
	data = request.get_json()

	category = (data.get("category", None)).title()
	language = data.get("language", None)
	sub_category = data.get("sub_category", None)
	new_category = data.get("new_category", None)
	filters = []
	if language:
		if ',' in language:
			languages = [lang.strip().lower() for lang in language.split(",")]
			language_filter = func.lower(Question.language).in_(languages)
		else:
			language_filter = func.lower(Question.language) == language.strip().lower()
		filters.append(language_filter)
	
	if sub_category:
		sub_category = sub_category.lower()
		if sub_category.lower() == "vegetables":
			
	
			allowed_vegetables = [
				"tomatoes", "carrots", "onions", "mushrooms", "eggplant", 
        "beetroot", "doodoo", "spinach", "cucumbers", "avocado", 
        "cabbage", "nakati", "ginger", "green pepper", "garlic", 
        "okra", "lettuce", "malakwang", "pepper"
				]
			if ',' in sub_category:
				sub_categories = [lang.strip().lower() for lang in sub_category.split(",")]
				sub_category_filter = func.lower(Question.animal_crop).in_(sub_categories)
				sub_category_filter = and_(sub_category_filter, func.lower(Question.animal_crop).in_(allowed_vegetables))
			else:
				sub_category_filter = func.lower(Question.animal_crop).in_(allowed_vegetables)
		else:
			if ',' in sub_category:
				sub_categories = [lang.strip().lower() for lang in sub_category.split(",")]
				sub_category_filter = func.lower(Question.animal_crop).in_(sub_categories)
			else:
				sub_category_filter = func.lower(Question.animal_crop) == sub_category.strip().lower()
		filters.append(sub_category_filter)


	matching_questions = Question.query.filter(
		Question.category.ilike(category),
		Question.rephrased == "actual",
    Question.reviewed == True,
    Question.answered.is_not(True),
		*filters
		).order_by(db.func.random()).first()

	if matching_questions is not None:
		return jsonify(jsonify_question(matching_questions)), HTTP_200_OK
	else:
		return jsonify({"message": "No questions available."}), HTTP_404_NOT_FOUND


@questions.post("/add_answer/<int:question_id>")
@jwt_required()
def add_answer(question_id):
	data = request.get_json()
	user_id = get_jwt_identity()
	answer_text = request.json["answer"].strip()

	question = Question.query.get(question_id)
	if not question:
		return jsonify({"message": "Question not found."}), HTTP_404_NOT_FOUND

	if answer_text and len(answer_text) > 7:
		new_answer = Answer(
			question_id=question_id,
			user_id=user_id,
			answer_text=answer_text,
			source="expert",
		)

		db.session.add(new_answer)
		question.answered = True
		question.answer_expert_one = user_id
		db.session.commit()

		return jsonify({"message": "Answer added successfully."}), HTTP_201_CREATED
	return jsonify({"message": "Failed to add answer."})

@questions.post("/review_and_answer/<int:question_id>")
@jwt_required()
def review_and_answer(question_id):
	user_id = get_jwt_identity()
	question = Question.query.get(question_id)

	if not question:
		return jsonify({"message": "Question not found."}), HTTP_404_NOT_FOUND

	data = request.get_json()
	answer_text = data.get("answer", "").strip()
	new_topic = data.get("topic")

	if answer_text and len(answer_text) > 4:
		new_answer = Answer(
				question_id=question_id,
				user_id=user_id,
				answer_text=answer_text,
				source="expert",
		)

		db.session.add(new_answer)
		question.answered = True
		question.answer_expert_one = user_id

		if question.topic:
			if new_topic:
				question.topic = (new_topic + ", " + question.topic)
		else:
			question.topic = new_topic

		question.reviewed = True
		question.correct = True
		question.reviewer_id = user_id

		db.session.commit()

		return jsonify({"message": "Answer added successfully and question attributes updated."}), HTTP_201_CREATED

	return jsonify({"message": "Failed to add answer or update question attributes."})

@questions.route("/incorrect/<int:question_id>", methods=["PUT"])
@jwt_required()
def mark_question_as_reviewed(question_id):
	user_id = get_jwt_identity()
	question = Question.query.get(question_id)

	if question:
		question.reviewed = True
		question.correct = False
		question.reviewer_id = user_id

		db.session.commit()

		return jsonify({"message": "Question attributes updated"})
	else:
		return jsonify({"message": "Question not found"})


@questions.route("/question_review/<int:question_id>", methods=["PATCH"])
@jwt_required()
def question_review(question_id):
	user_id = get_jwt_identity()
	question = Question.query.get(question_id)
	
	if question:

		question.reviewed = True
		question.correct = True 
		question.reviewer_id = user_id

		rephrased_data = request.json.get(
			"rephrased"
		)
		if rephrased_data:
			question.sentence = rephrased_data

		new_topic = request.json.get(
			"topic"
		)
		if question.topic:
			if new_topic:
				question.topic = (
					new_topic + ", " + question.topic
				)
		else:
			question.topic = new_topic 

		db.session.commit()

		return jsonify({"message": "Question attributes updated"})
	else:
		return jsonify({"message": "Question not found"})


@questions.route("/random_unanswered_question", methods=["GET"])
@jwt_required()
def get_random_unanswered_question():
	user_id = get_jwt_identity()

	# Get a random unanswered question for the user
	random_questions = Question.query.filter(
		Question.rephrased == "actual",
    Question.reviewed == True,
    Question.answered.is_not(True),
		Question.user_id == user_id
	).all()
	print(len(random_questions))
	questions_data = []
	if random_questions:
		for random_question in random_questions:
			question_data = {
				"id": random_question.id,
				"sentence": random_question.sentence,
				"language": random_question.language,
				"category": random_question.category,
				"sub_topic": random_question.animal_crop,
				"location": random_question.location,
				# "sub_topic": random_question.sub_topic,
			}
			questions_data.append(question_data)
		return jsonify(questions_data), 200
	else:
		return jsonify({"message": "No unanswered questions available"}), 404


@questions.route("/luganda", methods=["GET"])
@jwt_required()
def get_luganda_questions():
	luganda_questions = Question.query.filter(
		(Question.rephrased != "actual"),
		(Question.cleaned.is_(None) | (Question.cleaned != "t"))
		& (func.lower(Question.language) == "luganda")
	).all()

	if luganda_questions:
		questions_data = []
		for question in luganda_questions:
			question_data = {
				"id": question.id,
				"sentence": question.sentence,
				"language": question.language,
				"created_at": question.created_at.strftime("%Y-%m-%d %H:%M:%S"),
				"topics": question.topic,
				"sub_topic": question.sub_topic,
				"category": question.category,
				"animal_crop": question.animal_crop,
				"location": question.location,
				"cleaned": question.cleaned,
			}
			questions_data.append(question_data)

		return jsonify(questions_data), HTTP_200_OK
	else:
		return jsonify({"message": "No Luganda questions found"}), HTTP_404_NOT_FOUND


@questions.route("/english", methods=["GET"])
@jwt_required()
def get_english_questions():
	english_questions = Question.query.filter(
		(Question.rephrased != "actual"),
		(Question.cleaned.is_(None) | (Question.cleaned != "t"))
		& (func.lower(Question.language) == "english")
	).all()

	if english_questions:
		questions_data = []
		for question in english_questions:
			question_data = {
				"id": question.id,
				"sentence": question.sentence,
				"language": question.language,
				"created_at": question.created_at.strftime("%Y-%m-%d %H:%M:%S"),
				"topics": question.topic,
				"sub_topic": question.sub_topic,
				"category": question.category,
				"animal_crop": question.animal_crop,
				"location": question.location,
				"cleaned": question.cleaned,
			}
			questions_data.append(question_data)

		return jsonify(questions_data), HTTP_200_OK
	else:
		return jsonify({"message": "No Luganda questions found"}), HTTP_404_NOT_FOUND
	
@questions.route("/runyankole", methods=["GET"])
@jwt_required()
def get_runyankole_questions():
	verify_jwt_in_request()
	current_user = get_jwt_identity()
	is_admin = User.query.get(current_user)

	runya_questions = (Question.query
	.filter(Question.user_id != is_admin.id)
	.filter(func.lower(Question.language) == "runyankole")
	.all())


	if runya_questions:
		questions_data = []
		for question in runya_questions:
			question_data = {
				"id": question.id,
				"sentence": question.sentence,
				"language": question.language,
				"created_at": question.created_at.strftime("%Y-%m-%d %H:%M:%S"),
				"topics": question.topic,
				"sub_topic": question.sub_topic,
				"category": question.category,
				"animal_crop": question.animal_crop,
				"location": question.location,
				"cleaned": question.cleaned,
			}
			questions_data.append(question_data)

		return jsonify(questions_data), HTTP_200_OK
	else:
		return jsonify({"message": "No Runyankole questions found"}), HTTP_404_NOT_FOUND
	
@questions.route("/audios", methods=["GET"])
@jwt_required()
def audio_questions():
	
	audio_questions_list = []

	# for filename in allaudios:
	# 	question_detail = Question.query.filter(func.lower(Question.filename) == filename.lower()).first()

	# 	if question_detail:
	# 		user = User.query.get(question_detail.user_id)
	# 		if user:
	# 			user_name = f"{user.firstname} {user.lastname}"
     
	# 		audio_questions_list.append({
	# 			'id': question_detail.id,
	# 			"language": question_detail.language,
	# 			"created_at": question_detail.created_at.strftime("%Y-%m-%d %H:%M:%S"),
	# 			"topics": question_detail.topic,
	# 			"sub_topic": question_detail.sub_topic,
	# 			"category": question_detail.category,
	# 			"animal_crop": question_detail.animal_crop,
	# 			"location": question_detail.location,
	# 			'filename': question_detail.filename,
	# 			'username': user_name,
	# 			# 'file_content': get_audio_file_content(file_path)
	# 		})
	# 		print(len(audio_questions_list))
	# if len(audio_questions_list) > 0:
	# 	return jsonify(audio_questions_list)
	# else:
	return jsonify({"message": "No Audio questions found"}), HTTP_404_NOT_FOUND

@questions.route("/expertluganda", methods=["GET"])
@jwt_required()
def get_expert_luganda_questions():
	luganda_questions = Question.query.filter(
		(Question.rephrased == "actual")
		& (func.lower(Question.language) == "luganda")
	).all()

	if luganda_questions:
		questions_data = []
		for question in luganda_questions:
			question_data = {
				"id": question.id,
				"sentence": question.sentence,
				"language": question.language,
				"created_at": question.created_at.strftime("%Y-%m-%d %H:%M:%S"),
				"topics": question.topic,
				"sub_topic": question.sub_topic,
				"category": question.category,
				"animal_crop": question.animal_crop,
				"location": question.location,
			}
			questions_data.append(question_data)

		return jsonify(questions_data), HTTP_200_OK
	else:
		return jsonify({"message": "No Luganda expert questions found"}), HTTP_404_NOT_FOUND
	
@questions.route("/expertenglish", methods=["GET"])
@jwt_required()
def get_expert_english_questions():
	luganda_questions = Question.query.filter(
		(Question.rephrased == "actual")
		& (func.lower(Question.language) == "english")
	).all()

	if luganda_questions:
		questions_data = []
		for question in luganda_questions:
			question_data = {
				"id": question.id,
				"sentence": question.sentence,
				"language": question.language,
				"created_at": question.created_at.strftime("%Y-%m-%d %H:%M:%S"),
				"topics": question.topic,
				"sub_topic": question.sub_topic,
				"category": question.category,
				"animal_crop": question.animal_crop,
				"location": question.location,
			}
			questions_data.append(question_data)

		return jsonify(questions_data), HTTP_200_OK
	else:
		return jsonify({"message": "No English expert questions found"}), HTTP_404_NOT_FOUND
	
@questions.route("/expertrunyankole", methods=["GET"])
@jwt_required()
def get_expert_runyankole_questions():
	luganda_questions = Question.query.filter(
		(Question.rephrased == "actual")
		& (func.lower(Question.language) == "runyankole")
	).all()

	if luganda_questions:
		questions_data = []
		for question in luganda_questions:
			question_data = {
				"id": question.id,
				"sentence": question.sentence,
				"language": question.language,
				"created_at": question.created_at.strftime("%Y-%m-%d %H:%M:%S"),
				"topics": question.topic,
				"sub_topic": question.sub_topic,
				"category": question.category,
				"animal_crop": question.animal_crop,
				"location": question.location,
			}
			questions_data.append(question_data)

		return jsonify(questions_data), HTTP_200_OK
	else:
		return jsonify({"message": "No Runyankole expert questions found"}), HTTP_404_NOT_FOUND

@questions.route("/evaluated", methods=["GET"])
@jwt_required()
def get_evaluated_questions():
	
	matching_questions = (
		Question.query.filter(
			Question.ranking_count == 2)
		.all()
	)
	total_questions = len(matching_questions)
	print(total_questions)

	if matching_questions:
		questions_data = []
		for question in matching_questions:
			question_data = {
				"id": question.id,
				"sentence": question.sentence,
				"language": question.language,
				"created_at": question.created_at.strftime("%Y-%m-%d %H:%M:%S"),
				"topic": question.topic,
				"sub_topic": question.sub_topic,
				"category": question.category,
				"animal_crop": question.animal_crop,
				"location": question.location,
				"answers": []
			}

			for answer in question.answers:
				answer_data = {
					"id": answer.id,
					"answer_text": answer.answer_text,
					"source": answer.source,
					"relevance": answer.relevance,
					"coherence": answer.coherence,
					"fluency": answer.fluency,
					"context": answer.context,
					"created_at": answer.created_at.strftime("%Y-%m-%d %H:%M:%S"),
				}
				question_data["answers"].append(answer_data)

			questions_data.append(question_data)

		result_object = {
				"questions": questions_data,
				"total_questions": total_questions
		}
		print(len(question_data))
		return jsonify(result_object), HTTP_200_OK
	else:
		return jsonify({"message": "No questions available for ranking."}), HTTP_404_NOT_FOUND

@questions.route("/cleaning", methods=["GET"])
@jwt_required()
def clean_evaluated_questions():
	matching_questions = Question.query.filter(Question.ranking_count == 2).all()
	if matching_questions:
		for entry in matching_questions:
			for answer in entry.answers:
				if answer.relevance > 10:
					sum_of_digits = sum(int(digit) for digit in str(answer.relevance))
					answer.relevance = sum_of_digits
				if answer.coherence > 10:
					sum_of_digits = sum(int(digit) for digit in str(answer.coherence))
					answer.coherence = sum_of_digits
				if answer.fluency > 10:
					sum_of_digits = sum(int(digit) for digit in str(answer.fluency))
					answer.fluency = sum_of_digits
		db.session.commit()
		return jsonify({"message": "Values updated successfully."}), HTTP_200_OK
	else:
			return jsonify({"message": "No questions available for cleaning."}), HTTP_404_NOT_FOUND

@questions.route("/dataset_upload/", methods=["POST"])
@jwt_required()
def upload_excel_file():
	if request.method == "POST":
		file_excel = request.files.get("file")

		if file_excel and file_excel.filename.endswith(".xlsx"):
			try:
				# Read the Excel file using pandas
				df = pd.read_excel(file_excel)

				current_user = get_jwt_identity()
				dup_count = 0
				duplicates = []

				for _, row in df.iterrows():
					sentence = row.get("sentence")
					language = row.get("language")
					topic = row.get("topics", None)
					category = row.get("category", None)
					animal_crop = row.get("crop_animal", None)
					location = row.get("location", None)

					if Question.query.filter_by(sentence=sentence).first():
						dup_count += 1
						duplicates.append({"sentence": sentence})
					else:
						question = Question(
							sentence=sentence,
							language=language,
							user_id=current_user,
							topic=topic,
							category=category,
							animal_crop=animal_crop,
							location=location,
						)
						db.session.add(question)

				db.session.commit()

				num_questions = Question.query.filter_by(user_id=current_user).count()

				return (
					jsonify(
						{
							"num_questions": num_questions,
							"duplicate_questions": dup_count,
							"duplicates": duplicates,
						}
					),
					HTTP_200_OK,
				)
			except Exception as e:
				return jsonify({"message": str(e)}), HTTP_400_BAD_REQUEST
		else:
			return (
				jsonify(
					{"message": "Invalid file format. Please upload a .xlsx file."}
				),
				HTTP_400_BAD_REQUEST,
			)

@questions.route("/main_question_rank", methods=["POST"])
@jwt_required()
def main_question_rank():
	sub_category_map = {
    "poultry": ["chicken", "ducks", "guinea fowls", "turkeys"],
    "vegetables":  [
			"tomatoes", "carrots", "onions", "mushrooms", "eggplant", "beetroot",
			"doodo", "spinach", "cucumbers", "avocado", "cabbage", "nakati", "ginger",
			"green pepper", "garlic", "okra", "lettuce", "malakwang", "pepper", "sukuma wiiki",
			"kale", "hubiscus", "crops", "crop"
		],
		"cattle": ["cattle", "goat", "goats", "sheep"],
		"fish": ["fish", 'Fish'],
		"banana": ["banana", "bananas", "crop", "crops"],
		"fruits": ["watermelon", "pineapple", "mango", "sugarcane", "orange", "avocado", "passion fruit", "jack fruit", "paw paw", "guava", "lemon"],
		"cereals": ["maize", "sorghum", "millet", "rice", "wheat", "sim sim", "sesame"],
		"legumes": [ "soya beans", "beans", "peas", "groundnuts", "Gnuts", "ground nuts"],
		"piggery": ["pigs", 'animal', 'animals']
  }

	data = request.get_json()
	
	category = (data.get("category", None)).title()
	language = data.get("language", None)
	sub_category = data.get("sub_category", None)
	new_category = data.get("new_category", None)

	current_user = get_jwt_identity()

	filters = []
	random_question_data = None

	category_filter = func.lower(Question.category) == category

	if language:
		languages = [lang.strip().lower() for lang in language.split(",")]
		language_filter = func.lower(Question.language).in_(languages)
		filters.append(language_filter)

	if sub_category:
		sub_categories = [sc.strip().lower() for sc in new_category.split(",")]
		sub_category_filters = []
		
		for sub_category_name in sub_categories:
			sub_category_list = sub_category_map.get(sub_category_name)
			if sub_category_list:
				sub_category_filters.append( func.lower(Question.animal_crop).in_(sub_category_list))
			else:
				sub_category_filters.append(func.lower(Question.animal_crop) == sub_category_name)
		
		if sub_category_filters:
			filters.append(or_(*sub_category_filters))

	random_question = (
		Question.query.filter(
			Question.rephrased == "actual",
    	Question.answered.is_(True),
    	Question.finished.is_not(True),
			(~Question.answers.any(Answer.user_id == current_user)),
			Question.rank_expert_one != current_user,
			Question.ranking_count < 2,
			*filters)
		.all()
	)

	matching_questions = None
	if random_question:
		partial_ranked_qns = [q for q in random_question if q.ranking_count == 1]

		if partial_ranked_qns:
			matching_questions = random.sample(partial_ranked_qns, 1)[0]
		else:
			matching_questions = random.sample(random_question, 1)[0]
	
	if matching_questions:
		random_question_data = {
			"id": matching_questions.id,
			"sentence": matching_questions.sentence,
			"language": matching_questions.language,
			"created_at": matching_questions.created_at.strftime("%Y-%m-%d %H:%M:%S"),
			"topic": matching_questions.topic,
			"sub_topic": matching_questions.sub_topic,
			"category": matching_questions.category,
			"animal_crop": matching_questions.animal_crop,
			"location": matching_questions.location,
			"filename": matching_questions.filename,
		}

	    # Create a list to store answer data for each associated answer
		answer_list = []
		for answer in matching_questions.answers:
			answer_data = {
				"id": answer.id,
				"answer_text": answer.answer_text,
				"source": answer.source,
				"relevance": answer.relevance,
				"coherence": answer.coherence,
				"fluency": answer.fluency,
				"rank": answer.rank,
				"created_at": answer.created_at.strftime("%Y-%m-%d %H:%M:%S"),
			}
			answer_list.append(answer_data)

		random_question_data["answers"] = answer_list

	if random_question_data:
		result_object = {"random_question_data": random_question_data}
		return jsonify(result_object), HTTP_200_OK
	else:
		return jsonify({"message": "No questions available for ranking."}), HTTP_404_NOT_FOUND
	
def upload_to_bucket(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to a GCP storage bucket."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)
    print(f"File {source_file_name} uploaded to {destination_blob_name} in bucket {bucket_name}.")

	
@questions.route("/fetch_questions", methods=["GET"])
@jwt_required()
def fetch_questions():
	page = request.args.get('page', 1, type=int)
	per_page = request.args.get('per_page', 50, type=int)

	matching_questions = (
		Question.query.filter(
			Question.rephrased == "actual",
    	Question.reviewed == False
			)
		.paginate(page=page, per_page=per_page, error_out=False)
	)
	all = []
	random_question_data = None
	if matching_questions:
		for question in matching_questions:
			answers = [{'text': answer.answer_text, 'source': answer.source} for answer in question.answers]

			random_question_data = {
				"id": question.id,
				"sentence": question.sentence,
				"language": question.language,
				"topic": question.topic,
				"sub_topic": question.sub_topic,
				"category": question.category,
				"animal_crop": question.animal_crop,
				"location": question.location,
				"answers": answers
			}
			all.append(random_question_data)

	if all:
		pagination_details = {
			'total_pages': matching_questions.pages,
			'current_page': matching_questions.page,
			'per_page': per_page,
			'total_questions': matching_questions.total
    }

		return jsonify({'questions': all, 'pagination': pagination_details}), HTTP_200_OK
	else:
		return jsonify({"message": "No questions available."}), HTTP_404_NOT_FOUND


@questions.route("/store_answer_ranks", methods=["POST"])
@jwt_required()
def store_answer_ranks():
	user_id = get_jwt_identity()
	data = request.json
	question_id = data.get("questionId")
	rankings = data.get("rankings")

	if question_id is None or rankings is None:
		return jsonify({"message": "Invalid data format"}), HTTP_400_BAD_REQUEST

	question = Question.query.get(question_id)

	if question is None:
		return jsonify({"error": "Question not found"}), HTTP_404_NOT_FOUND

	ranking_count = 0
	try:
		for ranking in rankings:
			answer_id = ranking.get("answer_id")
			answer = Answer.query.get(answer_id)

			if answer:
				relevance = answer.relevance if answer.relevance is not None else 0
				coherence = answer.coherence if answer.coherence is not None else 0
				fluency = answer.fluency if answer.fluency is not None else 0
				
				relevance = relevance + chanelle(ranking.get("relevance"))
				coherence = coherence + chanelle(ranking.get("coherence"))
				fluency = fluency + chanelle(ranking.get("fluency"))
				
				# answer.context = ranking.get("context")
				if ranking.get("isFlagged"):
					answer.offensive = True

				answer.relevance = relevance
				answer.coherence = coherence
				answer.fluency = fluency
				answer.context = ranking.get("context")


		if question:
			if question.rank_expert_one is None:
				question.rank_expert_one = user_id
				question.ranking_count = 1
			else:
				question.rank_expert_two = user_id
				question.ranking_count = 2

			ranking_count += 1

		if ranking_count == 2 or question.ranking_count == 2:
			question.finished = True

		db.session.commit()
		return jsonify({"message": "Answer ranks stored successfully"}), HTTP_200_OK

	except Exception as e:
		db.session.rollback()
		return jsonify({"message": "Error storing answer ranks"}), HTTP_400_BAD_REQUEST


@questions.route("/expert-stats", methods=["GET"])
@jwt_required()
def question_stats():
	total_cleaned = Question.query.filter_by(cleaned=True, rephrased="actual").count()
	cleaned_and_reviewed = Question.query.filter_by(cleaned=True, reviewed=True, rephrased="actual").count()
	cleaned_reviewed_and_answered = Question.query.filter_by(
		cleaned=True, answered=True, rephrased="actual"
	).count()
	all_fields_true = Question.query.filter_by(cleaned=True, finished=True, rephrased="actual").count()
	experts = User.query.filter_by(role="expert").all()
	english_questions = Question.query.filter(
		Question.rephrased == "actual",
		Question.language.ilike("english")
	).count()
	luganda_questions = Question.query.filter(
		Question.rephrased == "actual",
		Question.language.ilike("luganda")
	).count()
	runyankole_questions = Question.query.filter(
		Question.rephrased == "actual",
		Question.language.ilike("runyankole")
	).count()

	fully_ranked = Question.query.filter(Question.ranking_count == 2).count()
	partial_ranked = Question.query.filter(Question.ranking_count == 1).count()

	expert_data = []
	for expert in experts:
		reviewed_questions_count = Question.query.filter_by(
			reviewer_id=expert.id
		).count()
		answers = Answer.query.filter_by(user_id=expert.id).count()

		ranked_answers = Question.query.filter((Question.rank_expert_one == expert.id) | (Question.rank_expert_two == expert.id)).count()

		expert_info = {
			"id": expert.id,
			"lastname": expert.lastname,
			"firstname": expert.firstname,
			"phone_number": expert.phone_number,
			"reviewed_questions_count": reviewed_questions_count,
			"answers_count": answers,
			"ranked_answers": ranked_answers,
			"language": expert.language,
			"expertise": expert.category,
			"sub_category": expert.sub_category,
			"new_category": expert.new_category,
			"created_at": expert.created_at,
		}

		expert_data.append(expert_info)

	return jsonify(
		{
			"total_cleaned": total_cleaned,
			"cleaned_and_reviewed": cleaned_and_reviewed,
			"cleaned_reviewed_and_answered": cleaned_reviewed_and_answered,
			"all_fields_true": all_fields_true,
			"experts": expert_data,
			"english_questions": english_questions,
			"luganda_questions": luganda_questions,
			"runyankole_questions": runyankole_questions,
			"fully_ranked": fully_ranked,
			"partial_ranked": partial_ranked
		}
	)


@questions.route("/user_answers", methods=["GET"])
@jwt_required()
def get_user_answers():
	user_id = get_jwt_identity()

	reviewed_questions_count = Question.query.filter_by(
		reviewer_id=user_id
	).count()

	questions_count = Question.query.filter(
		Question.answer_expert_one == user_id
	).count()

	answers = Answer.query.filter_by(user_id=user_id).count()

	ranked_answers = Question.query.filter((Question.rank_expert_one == user_id) | (Question.rank_expert_two == user_id)).count()

	user_answers = Answer.query.filter_by(user_id=user_id).all()
	answers_data = []

	for answer in user_answers:
		question = answer.question
		
		answers_data.append(
			{
				"id": answer.id,
				"answer_text": answer.answer_text,
				"created_at": answer.created_at,
				"question_id": answer.question_id,
				"sentence": question.sentence,
				"rank": question.ranking_count
			}
		)
	return jsonify({"questions_count":questions_count, "all_answers":answers_data, "answers": answers,"reviewed_questions": reviewed_questions_count,"ranked": ranked_answers})


@questions.route("/answers/<int:answer_id>", methods=["GET"])
@jwt_required()
def get_answer(answer_id):
	user_id = get_jwt_identity()


	answer = Answer.query.get(answer_id)
	if not answer:
		return jsonify({"error": "Answer not found"}), HTTP_404_NOT_FOUND

	if answer.user_id != user_id:
		return jsonify({"error": "Unauthorized access to answer details"}), 403

	question = Question.query.get(answer.question_id)
	if not question:
		return jsonify({"error": "Question not found"}), HTTP_404_NOT_FOUND

	response_data = {
		"answer_id": answer.id,
		"answer_text": answer.answer_text,
		"question_id": question.id,
		"question_text": question.sentence,
		"language": question.language,
		"animal_crop": question.animal_crop,
		"category": question.category,
		"topic": question.topic,
		"sub_topic": question.sub_topic,
	
	}

	return jsonify(response_data), HTTP_200_OK


@questions.route("/experts/<int:user_id>", methods=["GET"])
@jwt_required()
def get_expert_stats(user_id):
	answers = Answer.query.filter_by(user_id=user_id).all()
	if not answers:
		return jsonify({"error": "Answers not found"}), HTTP_404_NOT_FOUND

	answers_data = []
	for answer in answers:
		
		question = Question.query.get(answer.question_id)
		answers_data.append(
			{
				"answer_id": answer.id,
				"answer_text": answer.answer_text,
				"date": answer.created_at,
				"question_id": question.id,
				"question_text": question.sentence,
				"language": question.language,
				"animal_crop": question.animal_crop,
				"category": question.category,
				"topic": question.topic,
				"sub_topic": question.sub_topic,
			
			}
		)

	return jsonify(answers_data), HTTP_200_OK

@questions.route("/update_answer_text/<int:answer_id>", methods=["PUT"])
@jwt_required()
def update_answer_text(answer_id):
	answer = Answer.query.get(answer_id)
	if not answer:
		return jsonify({"message": "Answer not found"}), HTTP_404_NOT_FOUND
	new_answer_text = request.json.get("answer_text")

	if not new_answer_text:
		return jsonify({"message": "New answer_text not provided"}), HTTP_404_NOT_FOUND

	answer.answer_text = new_answer_text
	db.session.commit()

	return jsonify({"message": "Answer text updated successfully"}), HTTP_200_OK


@questions.route("/upload_json_answers/", methods=["GET"])
@jwt_required()
def upload_json_answers():

	current_user_id = get_jwt_identity()
	dup_count = 0
	duplicates = []

	for obj in embedded_json:
		sentence = obj.get("Questions")
		language = obj.get("language")
		topic = obj.get("Topics")
		sub_topic = obj.get("Sub topics")
		category = obj.get("Category")
		animal_crop = obj.get("animal_crop")
		location = obj.get("Location")

		# Check if the question already exists
		existing_qn = Question.query.filter_by(sentence=sentence, cleaned=True, rephrased="actual").first()
		if existing_qn:
				dup_count += 1
				duplicates.append({"sentence": sentence})
				existing_qn.animal_crop = animal_crop
				db.session.commit()

		else:
				question = Question(
						sentence=sentence,
						language=language,
						user_id=current_user_id,
						topic=topic,
						sub_topic=sub_topic,
						category=category,
						animal_crop=animal_crop,
						location=location,
						cleaned=True,
						rephrased="actual",
						reviewed=True,
						reviewer_id=1
				)
				db.session.add(question)
				db.session.commit()
				question_id = question.id

				response_categories = [
						"Llama2",
						"Bard",
						"Bing",
						"ChatGPT 3.5",
						"GPT 4",
				]
				for category in response_categories:
						response_value = obj.get(category)
						if response_value is not None:
								response = Answer(
										question_id=question_id,
										answer_text=response_value,
										source=category,
										user_id=current_user_id,
								)
								db.session.add(response)
								db.session.commit()

	response_data = {"duplicates_count": dup_count, "duplicates": duplicates}
	return jsonify(response_data), HTTP_200_OK


@questions.route("/issues", methods=["GET"])
@jwt_required()
def get_debug_answers():
	user_id = get_jwt_identity()
	updated_items = []
	invalid_values = []
	values_greater_than_10 = []
	
	for item in oldpa:
		item_id = item['id']
		db_item = Answer.query.get(item_id)
		
		if not db_item:
			continue  # If the answer is not found in the database, skip to the next
		coherence = item.get('coherence', None)
		relevance = item.get('relevance', None)
		fluency = item.get('fluency', None)
		if coherence == 1 or relevance == 1 or fluency == 1:
			invalid_values.append(item)
		elif coherence and coherence > 10 or relevance and relevance > 10 or fluency and fluency > 10:
			values_greater_than_10.append(item)
		else:
			if coherence:
				db_item.coherence = coherence
			if relevance:
				db_item.relevance = relevance
			if fluency:
				db_item.fluency = fluency
			updated_items.append(db_item)
			
	db.session.commit()
	return jsonify({
		'updated_items': [item.id for item in updated_items],
		'invalid_values': invalid_values,
		'values_greater_than_10': values_greater_than_10
	})
