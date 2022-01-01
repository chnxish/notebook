# React Redux MUI Next Node

## React

  + React是一个用于构建用户界面的JavaScript库。

  + React中使用样式

```javascript
// 行内样式
<div sstyle={{width: '40px', display: 'inline-block'}}></div>

// className
// 在React中设置class时使用className，然后引入对应的CSS文件
<div className="red"><div>
```

  + 工具链

    - 使用流行的React工具链，有助于完成如下的任务：

      - 扩展文件和组件的规模。

      - 使用来自npm的第三方库。

      - 尽早发现常用错误。

      - 在开发中实时编辑CSS和JS。

      - 优化生产输出。

    - 工具链选择：

      - 不需要工具链，可以考虑把React作为普通`<script>`标记添加到HTML页面中。

      - 使用`Create React App`，用于创建一个新的单页应用。

      - 使用`Next.js`，用于Node.js构建服务端渲染的网站。

    - 一组JavaScript构建工具链通常由这些组成：

      - package管理器，比如npm。它能让你充分利用庞大的第三方package的生态系统，并且轻松地安装或更新它们。

      - 打包器，比如webpack。它能让你编写模块化代码，并将它们组合在一起成为小的package，以优化加载时间。

      - 编译器，比如Babel。它能让你编写的新版本JavaScript代码，在旧版浏览器中依然能够工作。

  + 核心概念

    - JSX简介

      - 是一个JavaScript的语法扩展，可以很好地描述UI应该呈现出它应有交互的本质形式。

      - Babel会把JSX转译成一个名为`React.createElement()`函数调用。

    - 元素渲染

      - 元素是构成React应用的最小砖块。

      - 与浏览器的DOM元素不同，React元素是创建开销极小的普通对象。React DOM会负责更新DOM来与React元素保持一致。

      - React DOM会将元素和它的子元素与它们之前的状态进行比较，并只会进行必要的更新来使DOM达到预期的状态。

    - 组件和Props

      - 组件允许你将UI拆分成独立可复用的代码片段，并对每个片段进行独立构思。

      - 组件，从概念上类似于JavaScript函数。它接受任意的入参（即"props"），并返回用于描述页面展示内容的React元素。

      - 当React元素为用户自定义组件时，它会将JSX所接收的属性（attributes）以及子组件（children）转换为单个对象传递给组件，这个对象被称之为"props"。

      - React会将以小写字母开头的组件视为原生DOM标签，所以自定义组件名称必须以大写字母开头。

    - State和生命周期

      - 当组件第一次被渲染到DOM中的时候，这个过程在React中被称为挂载（mount）。当DOM中组件被删除的时候，这个过程在React中被称为卸载（unmount）。

      - 当组件挂载或卸载时就会去执行一些方法，这些方法叫做生命周期方法。如`componentDidMount()`，`componentWillUnmount()`函数等等。

      - 如果你把一个以组件构成的树想象成一个props的数据瀑布的话，那么每一个组件的state就像是在任意一点上给瀑布增加额外的水源，但是它只能向下流动。

    - 事件处理

      - React事件的命名采用小驼峰式，而不是纯小写。使用JSX语法时需要传入一个函数作为事件处理函数，而不是一个字符串。

    - 条件渲染

      - React中的条件渲染和JavaScript中的一样，使用JavaScript运算符if或者条件运算符去创建元素来表现当前的状态。

    - 列表和Key

      - Key帮助React识别哪些元素改变了，比如被添加或删除。因此应当给数组中的每一个元素赋予一个确定的标识。

      - 一个好的经验法则是：在`map()`方法中的元素需要设置key属性。

      - 数组元素中使用的key在其兄弟节点之间应该是独一无二的。然而，它们不需要是全局唯一的。

      - key会传递信息给React，但不会传递给你的组件。如果你的组件中需要使用key属性的值，请用其他属性名（如id）显式传递这个值。

    - 表单

      - 在HTML中，表单元素（如`<input>`，`textarea`，`<select>`）之类的表单元素通常自己维护state，并根据用户输入进行更新。而在React中，可变状态（mutable state）通常保存在组件的state属性中，并且只能通过使用`setState()`来更新。我们可以把两者结合起来，使React的state成为“唯一数据源”。渲染表单的React组件还控制着用户输入过程中表单发生的操作。被React以这种方式控制取值的表单输入元素就叫做“受控组件”。

    - 状态提升

      - 在React中，将多个组件中需要共享的state向上移动到它们的最近共同父组件中，便可实现共享state。这就是所谓的“状态提升”。

    - 组合和继承

      - React有十分强大的组合模式，推荐使用组合而非继承来实现组件间的代码重用。

      - Props和组合为你提供了清晰而安全地定制组件外观和行为的灵活方式。注意：组件可以接受任意props，包含基本数据类型，React元素以及函数。

      - 如果你想要在组件间复用非UI的功能，建议将其提取为一个单独的JavaScript模块，如函数、对象或者类。组件可以直接引入（import）而无需通过 extend 继承它们。

    - React哲学

      - React是用JavaScript构建快速响应的大型Web应用程序的首选方式。它在Facebook和Instagram上表现优秀。

      - 你可以自上而下或者自下而上构建应用：自上而下意味着首先编写层级较高的组件，自下而上意味着从最基本的组件开始编写。当你的应用比较简单时，使用自下而上的方式更方便；对于较为大型的项目来说，自下而上地构建，并同时为低层组件编写测试是更加简单的方式。

    - src: open programming/code/small_project/html_css_javascript/react-example project and run it, then visit localhost:3000

```javascript
/* jsx */
const user = {
  firstName: 'Harper',
  lastName: 'Perez'
};

function formatName(user) {
  return user.firstName + ' ' + user.lastName;
}

const element = <h1>Hello, {formatName(user)}!</h1>;

ReactDOM.render(
  element,
  document.getElementById('root')
);

/* 函数组件与class组件 */

class Welcome extends React.Component {
  render() {
    return <h1>Hello, {this.props.name}</h1>;
  }
}

function Welcome(props) {
  return <h1>Hello, {props.name}</h1>;
}

function App() {
  return (
    <div>
      <Welcome name="sara" />
      <Welcome name="Cahal" />
      <Welcome name="Edite" />
    </div>
  );
}

ReactDOM.render(
  <App />,
  document.getElementById('root')
);

/* State */
class Clock extends React.Component {
  // 构造函数是唯一给this.state赋值的地方
  // 应该使用setState()函数修改this.state的值
  constructor(props) {
    super(props);
    this.state = {date: new Date()};
  }

  componentDidMount() {
    this.timerID = setInterval(
      () => this.tick(),
      1000
    );
  }

  componentWillUnmount() {
    clearInterval(this.timerID);
  }

  tick() {
    this.setState({
      date: new Date()
    });
  }

  render() {
    return (
      <div>
        <h1>Hello, World!</h1>
        <h2>It is {this.state.date.toLocaleTimeString()}.</h2>
      </div>
    );
  }
}

ReactDOM.render(
  <Clock />,
  document.getElementById('root')
);

/* 事件处理 */

// 在传统的HTML中
<a href="#" onclick="console.log('This link was clicked.'); return false;">
  Click me
</a>

// 在React中，函数组件
function ActionLink() {
  function handleClick(e) {
    e.preventDefault();
    console.log('The link was clicked.');
  }

  return (
    <a href="#" onClick={handleClick}>
      Click me
    </a>
  );
}

// 在React中，class组件
class Toggle extends React.Component {
  constructor(props) {
    super(props);
    this.state = {isToggleOn: true};

    // 为了在回调中使用`this`，这个绑定是必不可少的
    this.handleClick = this.handleClick.bind(this);
  }

  handleClick() {
    this.setState(state => ({
      isToggleOn: !state.isToggleOn
    }));
  }

  render() {
    return (
      <button onClick={this.handleClick}>
        {this.state.isToggleOn ? 'ON' : 'OFF'}
      </button>
    );
  }
}

/* 条件渲染 */
function UserGreeting(props) {
  return <h1>Welcome back!</h1>
}

function GuestGreeting(props) {
  return <h1>Please sign up.</h1>
}

function Greeting(props) {
  const isLoggedIn = props.isLoggedIn;
  if (isLoggedIn) {
    return <UserGreeting />;
  } else {
    return <GuestGreeting />;
  }
}

ReactDOM.render(
  // Try changing to isLoggedIn={true}:
  <Greeting isLoggedIn={false} />,
  document.getElementById('root')
);

// 元素变量
function LoginButton(props) {
  return (
    <button onClick={props.onClick}>
      Login
    </button>
  );
}

function LogoutButton(props) {
  return (
    <button onClick={props.onClick}>
      Logout
    </button>
  );
}

class LoginControl extends React.Component {
  constructor(props) {
    super(props);
    this.state = {isLoggedIn: false};
    this.handleLoginClick = this.handleLoginClick.bind(this);
    this.handleLogoutClick = this.handleLogoutClick.bind(this);
  }

  handleLoginClick() {
    this.setState({isLoggedIn: true});
  }

  handleLogoutClick() {
    this.setState({isLoggedIn: false});
  }

  render() {
    const isLoggedIn = this.state.isLoggedIn;
    let button;
    if (isLoggedIn) {
      button = <LogoutButton onClick={this.handleLogoutClick} />;
    } else {
      button = <LoginButton onClick={this.handleLoginClick} />;
    }

    return (
      <div>
        <Greeting isLoggedIn={isLoggedIn} />
        {button}
      </div>
    );
  }
}

ReactDOM.render(
  <LoginControl />,
  document.getElementById('root')
);

// 与运算符&&
return (
  <div>
    <h1>Hello!</h1>
    {unreadMessages.length > 0 &&
      <h2>
        You have {unreadMessages.length} unread messages.
      </h2>
    }
  </div>
);

// 三目运算符
return (
  <div>
    The user is <b>{isLoggedIn ? 'currently' : 'not'}</b> logged in.
  </div>
);

// 阻止渲染
function WarningBanner(props) {
  if (!props.warn) {
    return null;
  }

  return (
    <div className="warning">
      Warning!
    </div>
  );
}

/* 列表和Key */
function NumberList(props) {
  const numbers = props.numbers;
  const listItems = numbers.map((number) => 
    <li key={number.toString()}>{number}</li>
  );
  return (
    <ul>{listItems}</ul>
  );
}

const numbers = [1, 2, 3, 4, 5];
ReactDOM.render(
  <NumberList numbers={numbers} />,
  document.getElementById('root')
);

// 在JSX中嵌入map()
function NumberList(props) {
  const numbers = props.numbers;
  return (
    <ul>
      {numbers.map((number) =>
        <ListItem key={number.toString()}
                  value={number} />
      )}
    </ul>
  );
}

/* 表单 */
// input tag
class NameForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {value: ''};
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({value: event.target.value});
  }

  handleSubmit(event) {
    alert('提交的名字：' + this.state.value);
    event.preventDefault();
  }

  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <label>
          名字:
          <input type="text" value={this.state.value} onChange={this.handleChange} />
        </label>
        <input type="submit" value="提交" />
      </form>
    );
  }
}

// textarea tag
class EssayForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      value: '请撰写一篇关于你喜欢的 DOM 元素的文章.'
    };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({value: event.target.value});
  }

  handleSubmit(event) {
    alert('提交的文章: ' + this.state.value);
    event.preventDefault();
  }

  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <label>
          文章:
          <textarea value={this.state.value} onChange={this.handleChange} />
        </label>
        <input type="submit" value="提交" />
      </form>
    );
  }
}

// select tag
class FlavorForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {value: 'coconut'};

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({value: event.target.value});
  }

  handleSubmit(event) {
    alert('你喜欢的风味是: ' + this.state.value);
    event.preventDefault();
  }

  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <label>
          选择你喜欢的风味:
          <select value={this.state.value} onChange={this.handleChange}>
            <option value="grapefruit">葡萄柚</option>
            <option value="lime">酸橙</option>
            <option value="coconut">椰子</option>
            <option value="mango">芒果</option>
          </select>
        </label>
        <input type="submit" value="提交" />
      </form>
    );
  }
}

// 处理多个输入
class Reservation extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      isGoing: true,
      numberOfGuests: 2
    };
    this.handleInputChange = this.handleInputChange.bind(this);
  }

  handleInputChange(event) {
    const target = event.target;
    const value = target.name === 'isGoing' ? target.checked : target.value;
    const name = target.name;

    this.setState({
      [name]: value
    });
  }

  render() {
    return (
      <form>
        <label>
          参与：
          <input
            name="isGoing"
            type="checkbox"
            checked={this.state.isGoing}
            onChange={this.handleInputChange} />
        </label>
        <br />
        <label>
          来宾人数:
          <input
            name="numberOfGuests"
            type="number"
            value={this.state.numberOfGuests}
            onChange={this.handleInputChange} />
        </label>
      </form>
    );
  }
}

/* 状态提升 */
function BoilingVerdict(props) {
  if (props.celsius >= 100) {
    return <p>The water would boil.</p>
  } else {
    return <p>The water would not boil.</p>
  }
}

function toCelsius(fahrenheit) {
  return (fahrenheit - 32) * 5 / 9;
}

function toFahrenheit(celsius) {
  return (celsius * 9 / 5) + 32;
}

function tryConvert(temperature, convert) {
  const input = parseFloat(temperature);
  if (Number.isNaN(input)) {
    return '';
  }
  const output = convert(input);
  // 保留三位小数并四舍五入
  const rounded = Math.round(output * 1000) / 1000;
  return rounded.toString();
}

const scaleNames = {
  c: 'Celsius',
  f: 'Fahrenheit'
}

class TemperatureInput extends React.Component {
  constructor(props) {
    super(props);
    this.handleChange = this.handleChange.bind(this);
  }

  handleChange(e) {
    this.props.onTemperatureChange(e.target.value);
  }

  render() {
    const temperature = this.props.temperature;
    const scale = this.props.scale;
    return (
      <fieldset>
        <legend>Enter temperature in {scaleNames[scale]}:</legend>
        <input value={temperature} onChange={this.handleChange} />
      </fieldset>
    );
  }
}

class Calculator extends React.Component {
  constructor(props) {
    super(props);
    this.handleCelsiusChange = this.handleCelsiusChange.bind(this);
    this.handleFahrenheitChange = this.handleFahrenheitChange.bind(this);
    this.state = {temperature: '', scale: 'c'};
  }

  handleCelsiusChange(temperature) {
    this.setState({scale: 'c', temperature});
  }

  handleFahrenheitChange(temperature) {
    this.setState({scale: 'f', temperature});
  }

  render() {
    const scale = this.state.scale;
    const temperature = this.state.temperature;
    const celsius = scale === 'f' ? tryConvert(temperature, toCelsius) : temperature;
    const fahrenheit = scale === 'c' ? tryConvert(temperature, toFahrenheit) : temperature;

    return (
      <div>
        <TemperatureInput
          scale="c"
          temperature={celsius}
          onTemperatureChange={this.handleCelsiusChange} />
        <TemperatureInput
          scale="f"
          temperature={fahrenheit}
          onTemperatureChange={this.handleFahrenheitChange} />
        <BoilingVerdict
          celsius={parseFloat(celsius)} />
      </div>
    );
  }
}

/* 组合 */
// 包含关系
function FancyBorder(props) {
  return (
    <div className={'FancyBorder FancyBorder-' + props.color}>
      {props.children}
    </div>
  );
}

function WelcomeDialog() {
  return (
    <FancyBorder color="blue">
      <h1 className="Dialog-title">
        Welcome
      </h1>
      <p className="Dialog-message">
        Thank you for visiting our spacecraft!
      </p>
    </FancyBorder>
  );
}

// 包含关系：利用自定义prop传递
function SplitPane(props) {
  return (
    <div className="SplitPane">
      <div className="SplitPane-left">
        {props.left}
      </div>
      <div className="SplitPane-right">
        {props.right}
      </div>
    </div>
  );
}

function App() {
  return (
    <SplitPane
      left={
        <Contacts />
      }
      right={
        <Chat />
      } />
  );
}

// 特例关系
function Dialog(props) {
  return (
    <FancyBorder color="blue">
      <h1 className="Dialog-title">
        {props.title}
      </h1>
      <p className="Dialog-message">
        {props.message}
      </p>
      {props.children}
    </FancyBorder>
  );
}

class SignUpDialog extends React.Component {
  constructor(props) {
    super(props);
    this.handleChange = this.handleChange.bind(this);
    this.handleSignUp = this.handleSignUp.bind(this);
    this.state = {login: ''};
  }

  render() {
    return (
      <Dialog title="Mars Exploration Program"
              message="How should we refer to you?">
        <input value={this.state.login}
               onChange={this.handleChange} />
        <button onClick={this.handleSignUp}>
          Sign Me Up!
        </button>
      </Dialog>
    );
  }

  handleChange(e) {
    this.setState({login: e.target.value});
  }

  handleSignUp() {
    alert(`Welcome aboard, ${this.state.login}!`);
  }
}
```
