import 'package:flutter/material.dart';

import '../config/application.dart';

final Map<String, Map<String, List<String>>> data = {
  'User Interface': {
    'Introduction To Widgets': ['Counter', 'Shopping List'],
    'Building Layouts': ['Places Of Interset'],
  },
  'Data & Backend': {
    'State Management': [],
    'Networking & HTTP': [],
  },
  'Accessibility & Internationalization': {},
  'Platform Integration': {},
  'Packages & Plugins': {},
};

class HomePage extends StatelessWidget {
  HomePage({Key? key, required this.title}) : super(key: key);

  final String title;

  @override
  Widget build(BuildContext context) {
    return DefaultTabController(
      length: data.keys.length,
      child: Scaffold(
        drawer: _buildNavBar(context),
        appBar: AppBar(
          bottom: TabBar(
            isScrollable: true,
            tabs: <Widget>[
              ...data.keys.map(((k) => Tab(text: k))),
            ],
          ),
          title: Text('Flutter Example'),
        ),
        body: TabBarView(
          children: <Widget>[
            ...data.values.map((v) => _buildCardList(context, v)),
          ],
        ),
      ),
    );
  }

  Widget _buildNavBar(BuildContext context) {
    return Drawer(
      child: ListView(
        // Remove padding
        padding: EdgeInsets.zero,
        children: <Widget>[
          UserAccountsDrawerHeader(
            accountName: Text('CHNxish'),
            accountEmail: Text('1095219764@qq.com'),
            currentAccountPicture: CircleAvatar(
              child: ClipOval(
                child: Image.asset(
                  'assets/images/profile.jpeg',
                  fit: BoxFit.cover,
                  width: 100,
                  height: 100,
                ),
              ),
            ),
            decoration: BoxDecoration(
              color: Theme.of(context).primaryColor,
              image: DecorationImage(
                fit: BoxFit.fill,
                image: AssetImage(
                  'assets/images/background_image.jpeg',
                ),
              ),
            ),
          ),
          ListTile(
            leading: Icon(Icons.favorite),
            title: Text('Favorites'),
            onTap: () => null,
          ),
          ListTile(
            leading: Icon(Icons.person),
            title: Text('Friends'),
            onTap: () => null,
          ),
          ListTile(
            leading: Icon(Icons.share),
            title: Text('Share'),
            onTap: () => null,
          ),
          ListTile(
            leading: Icon(Icons.notifications),
            title: Text('Request'),
            onTap: () => null,
            trailing: ClipOval(
              child: Container(
                color: Colors.red,
                width: 20,
                height: 20,
                child: Center(
                  child: Text(
                    '8',
                    style: TextStyle(
                      color: Colors.white,
                      fontSize: 12,
                    ),
                  ),
                ),
              ),
            ),
          ),
          Divider(),
          ListTile(
            leading: Icon(Icons.settings),
            title: Text('Settings'),
            onTap: () => null,
          ),
          ListTile(
            leading: Icon(Icons.description),
            title: Text('Policies'),
            onTap: () => null,
          ),
          Divider(),
          ListTile(
            title: Text('Exit'),
            leading: Icon(Icons.exit_to_app),
            onTap: () => null,
          ),
        ],
      ),
    );
  }

  Widget _buildCardList(BuildContext context, Map<String, List<String>> data) {
    return Column(
      children: <Widget>[
        SizedBox(
          height: 5,
        ),
        ...data.entries.map(
          (e) => Card(
            elevation: 0,
            child: Column(
              children: <Widget>[
                Container(
                  width: double.infinity,
                  height: 30,
                  padding: EdgeInsets.fromLTRB(5, 6, 0, 0),
                  color: Colors.black26,
                  child: Text(e.key),
                ),
                ...e.value.map(
                  (v) => GestureDetector(
                    onTap: () {
                      tappedList(context, v);
                    },
                    child: Container(
                      width: double.infinity,
                      height: 50,
                      padding: EdgeInsets.fromLTRB(15, 12, 0, 0),
                      decoration: BoxDecoration(
                        color: Colors.black12,
                        border: Border(
                          top: BorderSide(
                            width: 1,
                            color: Colors.grey,
                          ),
                        ),
                      ),
                      child: Text(v, style: TextStyle(fontSize: 20)),
                    ),
                  ),
                ),
              ],
            ),
          ),
        ),
      ],
    );
  }

  // actions
  void tappedList(BuildContext context, String key) {
    String route = '/display?key=$key';

    Application.router.navigateTo(context, route);
  }
}
