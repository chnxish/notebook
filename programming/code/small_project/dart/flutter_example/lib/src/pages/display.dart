import 'package:flutter/material.dart';

import '../components/components.dart';

Widget testCounter() {
  return Counter();
}

Widget testShoppingList() {
  return ShoppingList(products: ShoppingListTestData.data());
}

Widget testPlacesOfInterset() {
  return PlacesOfInterset(places: PlacesOfIntersetTestData.data());
}

typedef Widget ComponentCallback();

class DisplayPage extends StatelessWidget {
  DisplayPage({Key? key, required this.subcomponentName}) : super(key: key);

  String subcomponentName;

  @override
  Widget build(BuildContext context) {
    late ComponentCallback subcomponentCallback;

    if (subcomponentName == 'Counter') {
      subcomponentCallback = testCounter;
    } else if (subcomponentName == 'Shopping List') {
      subcomponentCallback = testShoppingList;
    } else if (subcomponentName == 'Places Of Interset') {
      subcomponentCallback = testPlacesOfInterset;
    }

    return Scaffold(
      appBar: AppBar(
        title: Text(subcomponentName),
      ),
      body: Container(
        child: subcomponentCallback(),
      ),
    );
  }
}
