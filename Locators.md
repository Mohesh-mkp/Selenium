
## <span style="color:teal;">**Types of Locators**
To fetch the location of an element, selenium uses different strategies. 

   * ID
   * Name
   * Link Text
   * Partial Link Text
   * Xpath
   * Tag Name
   * CSS Selector
   * Class Name


### [Explanation of locators](https://www.selenium.dev/documentation/webdriver/elements/locators/)

### **Locators with description**

| Locator             | Description                                                                                                             |
|---------------------|-------------------------------------------------------------------------------------------------------------------------|
| `class name`        | Locates elements whose class name contains the search value (compound class names are not permitted)                   |
| `css selector`      | Locates elements matching a CSS selector                                                                                |
| `id`                | Locates elements whose ID attribute matches the search value                                                           |
| `name`              | Locates elements whose NAME attribute matches the search value                                                         |
| `link text`         | Locates anchor elements whose visible text matches the search value                                                     |
| `partial link text` | Locates anchor elements whose visible text contains the search value. If multiple elements are matching, only the first one will be selected. |
| `tag name`          | Locates elements whose tag name matches the search value                                                                |
| `xpath`             | Locates elements matching an XPath expression     |


### **Relative Xpath Axes**

| AxisName                | Result                                                                                                 |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| `ancestor`              | Selects all ancestors (parent, grandparent, etc.) of the current node                                 |
| `ancestor-or-self`      | Selects all ancestors (parent, grandparent, etc.) of the current node and the current node itself      |
| `attribute`             | Selects all attributes of the current node                                                              |
| `child`                 | Selects all children of the current node                                                                |
| `descendant`            | Selects all descendants (children, grandchildren, etc.) of the current node                            |
| `descendant-or-self`    | Selects all descendants (children, grandchildren, etc.) of the current node and the current node itself|
| `following`             | Selects everything in the document after the closing tag of the current node                           |
| `following-sibling`     | Selects all siblings after the current node                                                            |
| `namespace`             | Selects all namespace nodes of the current node                                                        |
| `parent`                | Selects the parent of the current node                                                                 |
| `preceding`             | Selects all nodes that appear before the current node in the document, except ancestors, attribute nodes, and namespace nodes |
| `preceding-sibling`     | Selects all siblings before the current node                                                           |
| `self`                  | Selects the current node           |

