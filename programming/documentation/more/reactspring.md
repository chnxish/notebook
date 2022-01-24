# React-Spring

## React Spring

  + react-spring是一个基于spring-physics的动画库，应该可以满足你大部分与UI相关的动画需求。它为您提供了足够灵活的工具，可以自信地将您的想法转化为moving interfaces。

  + 这个库代表了一种现代的动画方法。它的灵感来自Christopher Chedeau的animated和Cheng Lou的react-motion。它继承了动画强大的插值和性能，以及react-motion的易用性。但是，虽然动画主要是命令性的，而react-motion主要是声明性的，但react-spring将两者联系起来。您会惊讶地发现，使用小型、显式的实用功能可以轻松地将静态数据转化为运动，这些实用功能不一定会影响您形成视图的方式。

  + react-spring是跨平台的，它支持web、react-native、react-native-web和几乎任何其他平台。

  + API

    - Common

      - Props

        - `useSpring({ from: { ... }, to: { ... }, delay: 100, onRest: () => ... });`

      - Configs

        - `useSpring({ config: { duration: 250 }, ... });`

      - Imperatives & Refs

    - Hooks

      - useSpring

      - useSprings

      - useTransition

      - useChain

      - useTrail

```javascript
/* Imperatives */
const [props, set, stop] = useSpring(() => ({ opacity: 1 }));

// Update spring with new props
set({ opacity: toggle ? 1 : 0 });

/* Refs */
const springRef = useSpringRef()

const { size, ...rest } = useSpring({
  ref: springRef,
  config: config.stiff,
  from: { size: '20%', background: 'hotpink' },
  to: {
    size: '100%',
    background: 'white',
  },
})
```

| Property | Type | Description |
| -------- | ---- | ----------- |
| from | obj | Base values, optional |
| to | obj/fn/array(obj) | Animates to ... |
| loop | obj/fn/bool | Looping settings, see loop prop for more details |
| delay | number/fn | Delay in ms before the animation starts. Also valid as a function for individual keys: key => delay |
| immediate | bool/fn | Prevents animation if true. Also valid as a function for individual keys: key => immediate |
| config | obj/fn | Spring config (contains mass, tension, friction, etc). Also valid as a function for individual keys: key => config |
| reset | bool | The spring starts to animate from scratch (from -> to) if set true |
| reverse | bool | "from" and "to" are switched if set true, this will only make sense in combination with the "reset" flag |
| cancel | bool/string/fn | When true, the cancel prop stops the animation of every animated value owned by the Controller that receives it. See cancel prop for more details |
| pause | bool | The pause prop literally freezes animations in time. |
| events | fn | A variety of event callbacks (see events for more information) |

| Event Name | Description |
| ---------- | ----------- |
| onStart | Callback when a spring or key is about to be animated |
| onChange | Frame by frame callback |
| onRest | Callback when a spring or key comes to a stand-still |
| onPause | Callback when a spring or key is paused |
| onResume | Callback when a spring or key is resumed |
| onDelayEnd | Callback when a spring or key has finished being delayed |
| onProps | Callback when a spring or key's props have been updated |

| Config Property | Default | Description |
| ---------------- | ------- | ----------- |
| mass | 1 | spring mass |
| tension | 170 | spring energetic load |
| friction | 26 | spring resistence |
| clamp | false | when true, stops the spring once it overshoots its boundaries |
| precision | 0.01 | how close to the end result the animated value gets before we consider it to be "there", this is important with spring animations |
| velocity | 0 | initial velocity (see v9 changelog for a breaking change). |
| easing | t => t | linear by default, you can use any easing you want, for instance d3-ease, we have included a variety of easings see here |
| damping | 1 | The damping ratio, which dictates how the spring slows down. Only works when frequency is defined. Defaults to 1. |
| progress | 0 | When used with duration, it decides how far into the easing function to start from. The duration itself is unaffected. |
| duration | undefined | if > than 0 will switch to a duration-based animation instead of spring physics, value should be indicated in milliseconds (e.g. duration: 250 for a duration of 250ms) |
| decay | undefined | number of decay rate. If passed true defaults to 0.998 |
| frequency | undefined | The natural frequency (in seconds), which dictates the number of bounces per second when no damping exists. When defined, tension is derived from this, and friction is derived from tension and damping. |
| round | undefined | While animating, round to the nearest multiple of this number. The from and to values are never rounded, as well as any value passed to the set method of an animated value. |
| bounce | undefined | When above zero, the spring will bounce instead of overshooting when exceeding its goal value. |
| restVelocity | undefined | The smallest velocity before the animation is considered to be "not moving". When undefined, precision is used instead. |

| Config Preset Property | Value |
| ---------------------- | ----- |
| config.default | { mass: 1, tension: 170, friction: 26 } | 
| config.gentle | { mass: 1, tension: 120, friction: 14 } |
| config.wobbly | { mass: 1, tension: 180, friction: 12 } |
| config.stiff | { mass: 1, tension: 210, friction: 20 } |
| config.slow | { mass: 1, tension: 280, friction: 60 } |
| config.molasses | { mass: 1, tension: 280, friction: 120 } |

  + src: open programming/code/small_project/html_css_javascript/react-example project and run it, then visit localhost:3000/react-spring-example

  + src: open programming/code/small_project/html_css_javascript/react-example project and run it, then visit localhost:3000/animated-card

  + src: open programming/code/small_project/html_css_javascript/react-example project and run it, then visit localhost:3000/animated-tree

  + src: open programming/code/small_project/html_css_javascript/react-example project and run it, then visit localhost:3000/draggable-list

  + src: open programming/code/small_project/html_css_javascript/react-example project and run it, then visit localhost:3000/masonry
