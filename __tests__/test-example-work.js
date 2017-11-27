import React from 'react';
import { configure, shallow } from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';
import ExampleWork, { WorkBubble } from '../js/example-work';

configure({ adapter: new Adapter() });

const myWork = [
  {
    'title': "Work Example 1",
    'image': {
      'desc': "example screenshot of a project involving code",
      'src': "images/example1.png",
      'comment': ""
    }
  },
  {
    'title': "Work Example 2",
    'image': {
      'desc': "example screenshot of a project involving chemistry",
      'src': "images/example2.png",
      'comment': `“Chemistry” by Surian Soosay is licensed under CC BY 2.0
           https://www.flickr.com/photos/ssoosay/4097410999`
    }
  }
]

describe("ExampleWork component", () => {
  let component = shallow(<ExampleWork work={myWork}/>);

  it("Should be a 'section' element", () => {
    expect(component.type()).toEqual('section');
  });
  it("Should contain as many children as there are work examples", () => {
    expect(component.find("WorkBubble").length).toEqual(myWork.length);
  });
});

describe("WorkBubble component", () => {
  let component = shallow(<WorkBubble example={myWork[1]}/>);
  let images = component.find("img");

  it("Should contain a single 'img' element", () => {
    expect(images.length).toEqual(1);
  });

  it("Should have the image src set corectly", () => {
    expect(images.getElement(0).props.src).toEqual(myWork[1].image.src);
  });
});
